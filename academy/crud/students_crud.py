from academy.datamodel.students import Students
from academy.datamodel.teachers import Teachers
from academy.datamodel.teachers_preferences_and_responsibilities import Teachers_pref_resp
from academy.db_utilities.session import AcademySession


def add_new_student(*args):
    with AcademySession.get_session() as session:
        if len(args) < 4:
            raise ValueError('Incorrect number of values for add_new_student')

        name = args[0]
        age = int(args[1])
        subject = args[2]
        teacher_id = args[3]

        teacher_exists = session.query(Teachers.id).filter(Teachers.id == teacher_id).scalar()
        if not teacher_exists:
            raise ValueError(f'Incorrect teacher_id {teacher_id} for add_new_student')

        query_1 = session.query(Teachers.language_for_programming).distinct().all()
        query_2 = session.query(Teachers.speciality).distinct().all()

        valid_languages = {item[0] for item in query_1 if item[0] is not None}
        valid_specialities = {item[0] for item in query_2 if item[0] is not None}

        if subject not in valid_languages and subject not in valid_specialities:
            raise ValueError(f'Subject {subject} is not valid')

        teacher_pref_resp = session.query(Teachers_pref_resp). \
            filter(Teachers_pref_resp.preference_id_for_teachers == teacher_id).first()

        if teacher_pref_resp and teacher_pref_resp.age_for_training:
            age_range = teacher_pref_resp.age_for_training.split('-')
            if len(age_range) != 2:
                raise ValueError(f'Invalid age range format: {teacher_pref_resp.age_for_training}')

            try:
                min_age = int(age_range[0])
                max_age = int(age_range[1])
            except ValueError:
                raise ValueError(f'Invalid age range values: {teacher_pref_resp.age_for_training}')

            if not (min_age <= age <= max_age):
                raise ValueError(f'Student age {age} is not within the allowed range {min_age}-{max_age}')

        existing_record = session.query(Students). \
            filter(Students.name == name).first()
        if existing_record:
            existing_record.name = name
            existing_record.age = age
            existing_record.subject = subject
            existing_record.id = teacher_id
        else:
            new_student = Students(
                name=name,
                age=age,
                subject=subject,
                teacher_id=teacher_id
            )
            session.add(new_student)
        session.commit()
