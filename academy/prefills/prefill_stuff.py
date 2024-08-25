from datetime import datetime
from academy.datamodel.staff import Staff
from academy.db_utilities.session import AcademySession


def prefill_staff():
    with AcademySession.get_session() as session:
        staff_data = [
            Staff(
                name='Daniil Amoshiy',
                age=17,
                gender='Male',
                speciality='Director',
                work_mail='kvakva@gmail.com',
                birthday=datetime.strptime('13.02.2007', '%d.%m.%Y'),
                start_work=datetime.strptime('01.01.2024', '%d.%m.%Y'),
                salary=120000
            ),
            Staff(
                name='Alina Kuznetsova',
                age=18,
                gender='Female',
                speciality='Deputy Director',
                work_mail='AlinRika@gmail.com',
                birthday=datetime.strptime('04.05.2006', '%d.%m.%Y'),
                start_work=datetime.strptime('01.01.2024', '%d.%m.%Y'),
                salary=60000
            ),
            Staff(
                name='George Oganesyan',
                age=22,
                gender='Male',
                speciality='Accountant',
                work_mail='g_Ogan@gmail.com',
                birthday=datetime.strptime('04.02.2002', '%d.%m.%Y'),
                start_work=datetime.strptime('23.01.2024', '%d.%m.%Y'),
                salary=40000
            ),
            Staff(
                name='Ivan Popov',
                age=34,
                gender='Male',
                speciality='Student Recruitment Manager',
                work_mail='Iv_Pop@gmail.com',
                birthday=datetime.strptime('03.03.1990', '%d.%m.%Y'),
                start_work=datetime.strptime('13.02.2024', '%d.%m.%Y'),
                salary=10000
            ),
            Staff(
                name='Nikolay Volkov',
                age=25,
                gender='Male',
                speciality='Security',
                work_mail='---',
                birthday=datetime.strptime('12.06.1999', '%d.%m.%Y'),
                start_work=datetime.strptime('05.04.2024', '%d.%m.%Y'),
                salary=15000
            ),
            Staff(
                name='Sergey Novikov',
                age=20,
                gender='Male',
                speciality='Helper',
                work_mail='Serg_034@gmail.com',
                birthday=datetime.strptime('13.06.2004', '%d.%m.%Y'),
                start_work=datetime.strptime('26.01.2024', '%d.%m.%Y'),
                salary=15000
            ),
            Staff(
                name='Ekaterina Sokolova',
                age=28,
                gender='Female',
                speciality='Manager',
                work_mail='Ketrin_228@gmail.com',
                birthday=datetime.strptime('10.07.2024', '%d.%m.%Y'),
                start_work=datetime.strptime('04.03.2024', '%d.%m.%Y'),
                salary=15000
            )
        ]
        session.add_all(staff_data)
        session.commit()
