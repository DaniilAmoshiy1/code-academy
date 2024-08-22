from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(
        prog='Code academy arguments',
        description='This is a project that was transferred from SQL to Python via SQLAlchemy',
    )
    parser.add_argument('-p', '--prefill', action='store_true', help='Prefill the database.')
    parser.add_argument(
        '-ns',
        '--new-staff',
        nargs='+',
        help='Here you can add a new staff, in strict order: name, age,\
            gender, speciality, work_email, birthday, Optional[start_work], salary'
    )
    parser.add_argument(
        '-sr',
        '--staff-requirements',
        nargs='+',
        help='Here you can add a new staff preferences and responsibilities, in\
             strict order: staff_id, time_for_working, day_for_working, language_to_speak'
    )


    return parser.parse_args()
