from academy.datamodel import Teachers_pref_resp
from academy.datamodel import Teachers
from academy.db_utilities import AcademySession


def add_new_teacher_pref_resp(*args):
    if len(args) < 5:
        raise ValueError('Incorrect number of values for add_new_teacher_pref_resp')

    with AcademySession.get_session() as session:
        preference_id_for_teachers = args[0]
        day_for_working = args[1]
        time_for_working = args[2]
        language_to_speak = args[3]
        age_for_training = args[4] if len(args) == 6 else None
        number_of_trainees = args[5] if len(args) == 6 else args[4]

        staff_exists = session.query(Teachers).filter(Teachers.id == preference_id_for_teachers).first()
        if not staff_exists:
            raise ValueError('The id that was specified does not exist in the table '
                             'teachers_preferences_and_responsibilities')

        existing_record = session.query(Teachers_pref_resp). \
            filter(Teachers_pref_resp.preference_id_for_teachers == preference_id_for_teachers).first()
        if existing_record:
            existing_record.day_for_working = day_for_working
            existing_record.time_for_working = time_for_working
            existing_record.language_to_speak = language_to_speak
            existing_record.age_for_training = age_for_training if len(args) == 6 else None
            existing_record.number_of_trainees = number_of_trainees if len(args) == 6 else args[4]
        else:
            new_teacher_pref_resp = Teachers_pref_resp(
                preference_id_for_teachers=preference_id_for_teachers,
                day_for_working=day_for_working,
                time_for_working=time_for_working,
                language_to_speak=language_to_speak,
                age_for_training=age_for_training,
                number_of_trainees=number_of_trainees
            )
            session.add(new_teacher_pref_resp)
        session.commit()
