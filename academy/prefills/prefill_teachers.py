from datetime import datetime
from academy.datamodel.teachers import Teachers
from academy.db_utilities.session import AcademySession


def prefill_teachers():
    with AcademySession.get_session() as session:
        teachers_data = [
            Teachers(
                name='Roman Voronov',
                age=33,
                gender='Male',
                birthday=datetime.strptime('25.07.2024', '%d.%m.%Y'),
                salary=30000,
                work_experience_in_years=33,
                language_for_programming='Python intro/professional, SQL, C++',
                rating=5.0
            ),
            Teachers(
                name='Gevorg Oganesyan',
                age=23,
                gender='Male',
                birthday=datetime.strptime('12.07.2001', '%d.%m.%Y'),
                salary=25000,
                work_experience_in_years=5,
                language_for_programming='JavaScript, C++',
                rating=4.8
            ),
            Teachers(
                name='Laila Che(not full name)',
                age=19,
                gender='Female',
                birthday=datetime.strptime('23.05.2005', '%d.%m.%Y'),
                salary=25000,
                work_experience_in_years=4,
                language_for_programming='C#, Java',
                rating=4.7
            ),
            Teachers(
                name='Aleksey Shukanov',
                age=25,
                gender='Male',
                birthday=datetime.strptime('16.04.1999', '%d.%m.%Y'),
                salary=25000,
                work_experience_in_years=3,
                speciality='DevOps',
                rating=4.5
            ),
            Teachers(
                name='Dmitry Andreev',
                age=28,
                gender='Male',
                birthday=datetime.strptime('13.01.1996', '%d.%m.%Y'),
                salary=25000,
                work_experience_in_years=7,
                language_for_programming='SQL professional',
                rating=4.7
            ),
            Teachers(
                name='Egor Borisov',
                age=45,
                gender='Male',
                birthday=datetime.strptime('16.09.1979', '%d.%m.%Y'),
                salary=15000,
                work_experience_in_years=15,
                language_for_programming='PHP',
                speciality='Game/Web Design, HTML',
                rating=4.2
            ),
            Teachers(
                name='Anastasiya Krasnova',
                age=143,
                gender='Female',
                birthday=datetime.strptime('01.02.1881', '%d.%m.%Y'),
                salary=10000,
                work_experience_in_years=2,
                language_for_programming='Python',
                rating=3.4
            ),
            Teachers(
                name='Olivia Johnson',
                age=56,
                gender='Female',
                birthday=datetime.strptime('18.11.1968', '%d.%m.%Y'),
                salary=17000,
                work_experience_in_years=9,
                language_for_programming='CSS, Swift',
                speciality='System Admin, Data Analyst, HTML',
                rating=4.0
            )
        ]
        session.add_all(teachers_data)
        session.commit()
