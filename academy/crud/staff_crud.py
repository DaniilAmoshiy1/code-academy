from datetime import datetime

from academy.datamodel.staff import Staff
from academy.db_utilities.session import AcademySession


def add_new_staff(*args):
    if len(args) < 7 or len(args) > 8:
        raise ValueError('Incorrect number of arguments for new staff')

    name = args[0]
    age = args[1]
    gender = args[2]
    speciality = args[3]
    work_email = args[4]
    birthday = args[5]
    start_work = args[6] if len(args) == 8 else None
    salary = args[7] if len(args) == 8 else args[6]

    birthday = datetime.strptime(birthday, '%d/%m/%Y')
    if start_work:
        start_work = datetime.strptime(start_work, '%d/%m/%Y')
    else:
        start_work = datetime(2024, 1, 1)

    new_staff = Staff(
        name=name,
        age=int(age),
        gender=gender,
        speciality=speciality,
        work_email=work_email,
        birthday=birthday,
        start_work=start_work,
        salary=int(salary)
    )

    with AcademySession.get_session() as session:
        session.add(new_staff)
        session.commit()
