from academy.datamodel.staff import Staff
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
        session.add(a_staff)
        session.commit()
