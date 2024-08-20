from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(
        prog='Code academy arguments',
        description='This is a project that was transferred from SQL to Python via SQLAlchemy',
    )
    parser.add_argument(
        '-ns',
        '--new-staff',
        nargs='+',
        help='Here you can add a new employee, in strict order: name, age,\
            gender, speciality, work_email, birthday, Optional[start_work], salary'
    )

    return parser.parse_args()
