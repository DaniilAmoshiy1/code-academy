from academy.datamodel.staff import Staff
from academy.datamodel.staff_preferences_and_responsibilities import Staff_pref_resp
from academy.datamodel.teachers import Teachers
from academy.datamodel.teachers_preferences_and_responsibilities import Teachers_pref_resp
from .session import AcademySession
from datetime import datetime


def prefill_database():
    birthday_str = '13/02/2007'
    birthday_date = datetime.strptime(birthday_str, '%d/%m/%Y')
    birthday_teacher_str = '25/07/2024'
    birthday_teacher_date = datetime.strptime(birthday_teacher_str, '%d/%m/%Y')
    with AcademySession.get_session() as session:
        a_staff = Staff(
            name='Daniil Amoshiy',
            age=17,
            gender='Male',
            speciality='Director',
            work_email='daniil@gmail.com',
            birthday=birthday_date,
            salary=20000
        )

        a_staff_pref_resp = Staff_pref_resp(
            staff_id=1,
            time_for_working='9:00 - 17:00',
            day_for_working='Monday, Tuesday, Friday',
            language_to_speak='Russian, English'
        )

        a_teacher = Teachers(
            name='Roman Voronov',
            age=34,
            gender='Male',
            birthday=birthday_teacher_date,
            salary=30000,
            work_experience_in_years=33,
            speciality=None,
            language_for_programming='Python',
        )

        a_teacher_pref_resp = Teachers_pref_resp(
            preference_id_for_teachers=1,
            day_for_working='Tuesday',
            time_for_working='12:00 - 22:00',
            language_to_speak='French',
            age_for_training='12-45',
            number_of_trainees=6
        )

        all_items = [a_staff, a_staff_pref_resp, a_teacher, a_teacher_pref_resp]
        session.add_all(all_items)
        session.commit()

