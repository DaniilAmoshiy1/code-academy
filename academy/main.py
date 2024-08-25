from .arguments import parse_arguments
from .crud import (
    get_recent_entries,
    add_new_staff,
    add_new_staff_pref_resp,
    add_new_student,
    add_new_teacher,
    add_new_teacher_pref_resp
)
from .db_utilities import (
    prefill_database,
    print_entries,
    reset_db,
    setup_db,
)
from .datamodel import (
    Teachers,
    Staff,
    Staff_pref_resp,
    Teachers_pref_resp,
    Students
)


def main():
    arguments = parse_arguments()

    setup_db()

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
        case _ if arguments.teachers:
            latest_teachers = get_recent_entries(Teachers, page=arguments.page)
            print_entries(latest_teachers)
        case _ if arguments.students:
            latest_students = get_recent_entries(Students, page=arguments.page)
            print_entries(latest_students)
        case _ if arguments.staff:
            latest_staff = get_recent_entries(Staff, page=arguments.page)
            print_entries(latest_staff)
        case _ if arguments.staff_preferences:
            latest_staff_pref_resp = get_recent_entries(Staff_pref_resp, page=arguments.page)
            print_entries(latest_staff_pref_resp)
        case _ if arguments.teacher_preferences:
            latest_teacher_pref_resp = get_recent_entries(Teachers_pref_resp, page=arguments.page)
            print_entries(latest_teacher_pref_resp)
        case _ if arguments.reset:
            reset_db()
        case _:
            setup_db()


if __name__ == '__main__':
    main()
