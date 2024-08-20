from academy.db_utilities.prefill import prefill_database
from academy.db_utilities.setup import setup_db, reset_db
from academy.arguments import parse_arguments
from academy.crud.staff_crud import add_new_staff


def main():
    arguments = parse_arguments()
    reset_db()
    setup_db()
    prefill_database()

    if arguments.new_staff:
        try:
            add_new_staff(*arguments.new_staff)
        except Exception as e:
            print(f"Error adding new staff: {e}")


if __name__ == '__main__':
    main()
