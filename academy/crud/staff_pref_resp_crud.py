from academy.datamodel.staff_preferences_and_responsibilities import Staff_pref_resp
from academy.datamodel.staff import Staff
from academy.db_utilities.session import AcademySession


def add_new_staff_pref_resp(*args):
    with AcademySession.get_session() as session:
        if len(args) < 4 or len(args) > 4:
            raise ValueError('Incorrect number of arguments for add_new_staff_pref_resp')

        staff_id = args[0]
        time_for_working = args[1]
        day_for_working = args[2]
        language_to_speak = args[3]

        staff_exists = session.query(Staff).filter(Staff.id == staff_id).first()
        if not staff_exists:
            raise ValueError('The id that was specified does not exist in the table staff.')

        existing_record = session.query(Staff_pref_resp).filter(Staff_pref_resp.staff_id == staff_id).first()

        if existing_record:
            existing_record.time_for_working = time_for_working
            existing_record.day_for_working = day_for_working
            existing_record.language_to_speak = language_to_speak
        else:
            new_staff_pref_resp = Staff_pref_resp(
                staff_id=staff_id,
                time_for_working=time_for_working,
                day_for_working=day_for_working,
                language_to_speak=language_to_speak
            )
            session.add(new_staff_pref_resp)
        session.commit()
