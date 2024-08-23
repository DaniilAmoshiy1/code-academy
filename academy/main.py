from academy.db_utilities.prefill import prefill_database
from academy.db_utilities.setup import setup_db, reset_db
from academy.arguments import parse_arguments
from academy.crud.staff_crud import add_new_staff
from academy.crud.staff_pref_resp_crud import add_new_staff_pref_resp
from academy.crud.teachers_crud import add_new_teacher
from academy.crud.teachers_pref_resp_crud import add_new_teacher_pref_resp


def main():
    arguments = parse_arguments()
    if arguments.prefill:
        reset_db()
    setup_db()
    if arguments.prefill:
        prefill_database()

    if arguments.new_staff:
        add_new_staff(*arguments.new_staff)

    if arguments.staff_requirements:
        add_new_staff_pref_resp(*arguments.staff_requirements)

    if arguments.new_teacher:
        add_new_teacher(*arguments.new_teacher)

    if arguments.teacher_requirements:
        add_new_teacher_pref_resp(*arguments.teacher_requirements)


if __name__ == '__main__':
    main()
