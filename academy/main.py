from .arguments import parse_arguments
from .crud import (
    add_new_staff,
    add_new_staff_pref_resp,
    add_new_student,
    add_new_teacher,
    add_new_teacher_pref_resp
)
from .db_utilities import (
    prefill_database,
    reset_db,
    setup_db,
)


def main():
    arguments = parse_arguments()

    match arguments:
        case _ if arguments.prefill:
            reset_db()
            setup_db()
            prefill_database()
        case _ if arguments.new_staff:
            add_new_staff(*arguments.new_staff)
        case _ if arguments.staff_requirements:
            add_new_staff_pref_resp(*arguments.staff_requirements)
        case _ if arguments.new_teacher:
            add_new_teacher(*arguments.new_teacher)
        case _ if arguments.teacher_requirements:
            add_new_teacher_pref_resp(*arguments.teacher_requirements)
        case _ if arguments.add_student:
            add_new_student(*arguments.add_student)
        case _:
            setup_db()


if __name__ == '__main__':
    main()
