from datetime import datetime
import random

from academy.datamodel.teachers import Teachers
from academy.db_utilities.session import AcademySession


def add_new_teacher(*args):
    with AcademySession.get_session() as session:
        if len(args) < 5:
            raise ValueError('Incorrect number of values for add_new_teacher')

        name = args[0]
        age = args[1]
        gender = args[2]
        birthday = args[3] if len(args) > 3 else None
        salary = args[4] if len(args) > 4 else 5000
        work_experience_in_years = args[5] if len(args) > 5 else 0
        speciality = args[6] if len(args) > 6 else None
        language_for_programming = args[7] if len(args) > 7 else None
        rating = args[8] if len(args) > 8 else round(random.uniform(2.5, 5.0), 1)

        birthday = datetime.strptime(birthday, '%d/%m/%Y')


        new_teacher = Teachers(
            name=name,
            age=age,
            gender=gender,
            birthday=birthday,
            salary=salary,
            work_experience_in_years=work_experience_in_years,
            speciality=speciality,
            language_for_programming=language_for_programming,
            rating=rating
        )

        session.add(new_teacher)
        session.commit()
