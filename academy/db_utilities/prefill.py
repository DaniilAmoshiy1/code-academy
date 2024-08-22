from academy.datamodel.staff import Staff
from academy.datamodel.staff_preferences_and_responsibilities import Staff_pref_resp
from .session import AcademySession
from datetime import datetime


def prefill_database():
    birthday_str = '13/02/2007'
    birthday_date = datetime.strptime(birthday_str, '%d/%m/%Y')
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
        all_items = [a_staff, a_staff_pref_resp]
        session.add_all(all_items)
        session.commit()
