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
            gender, speciality, work_email, birthday, [start_work], salary'
    )
    parser.add_argument(
        '-sr',
        '--staff-requirements',
        nargs='+',
        help='Here you can add/edit a [new] staff preferences and responsibilities, in\
             strict order: staff_id, time_for_working, day_for_working, language_to_speak'
    )
    parser.add_argument(
        '-nt',
        '--new-teacher',
        nargs='+',
        help='Here you can add a new teacher in strict order: name, age, gender, \
            [birthday], [salary], [work_experience_in_years], [speciality], \
            [language_for_programming], [rating]'
    )
    parser.add_argument(
        '-tr',
        '--teacher-requirements',
        nargs='+',
        help='Here you can add/edit a [new] teacher preferences and responsibilities, in \
             strict order: preference_id_for_teachers, day_for_working, time_for_working, \
             language_to_speak, [age_for_training], number_of_trainees'
    )
    parser.add_argument(
        '-as',
        '--add-student',
        nargs='+',
        help='Here you can add/edit a [new] student in strict order: name, age, subject, \
            teacher_id'

    )
    parser.add_argument(
        '-t',
        '--teachers',
        action='store_true',
        help='See latest teachers'
    )
    parser.add_argument(
        '-st',
        '--students',
        action='store_true',
        help='See latest students'
    )
    parser.add_argument(
        '-s',
        '--staff',
        action='store_true',
        help='See latest staff'
    )
    parser.add_argument(
        '-sp',
        '--staff-preferences',
        action='store_true',
        help='See latest staff preferences and responsibilities'
    )
    parser.add_argument(
        '-tp',
        '--teacher-preferences',
        action='store_true',
        help='See latest teacher preferences and responsibilities'
    )
    parser.add_argument(
        '-pg',
        '--page',
        type=int,
        default=1,
        help='Specify the page number for pagination (default is 1)'
    )
    parser.add_argument(
        '-r',
        '--reset',
        action='store_true',
        help='Reset database'
    )

    return parser.parse_args()
