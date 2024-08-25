from academy.datamodel.staff_preferences_and_responsibilities import Staff_pref_resp
from academy.db_utilities.session import AcademySession


def prefill_staff_pref_resp():
    with AcademySession.get_session() as session:
        staff_pref_data = [
            Staff_pref_resp(
                staff_id=1,
                time_for_working='9:00 - 17:00',
                day_for_working='Monday, Tuesday, Friday',
                language_to_speak='Russian'
            ),
            Staff_pref_resp(
                staff_id=2,
                time_for_working='8:00 - 20:00',
                day_for_working='Wednesday, Thursday, Saturday, Sunday',
                language_to_speak='English, Russian'
            ),
            Staff_pref_resp(
                staff_id=3,
                time_for_working='8:00 - 19:00',
                day_for_working='Monday - Friday',
                language_to_speak='English, Russian'
            ),
            Staff_pref_resp(
                staff_id=4,
                time_for_working='13:00 - 21:00',
                day_for_working='Friday',
                language_to_speak='English, Russian, French'
            ),
            Staff_pref_resp(
                staff_id=5,
                time_for_working='24h',
                day_for_working='All days',
                language_to_speak='English'
            ),
            Staff_pref_resp(
                staff_id=6,
                time_for_working='8:00 - 20:00',
                day_for_working='Monday - Friday',
                language_to_speak='English, Russian, French, Italian, Spanish, Ukrainian'
            ),
            Staff_pref_resp(
                staff_id=7,
                time_for_working='9:00 - 18:00',
                day_for_working='Monday - Friday',
                language_to_speak='Russian, English'
            )
        ]
        session.add_all(staff_pref_data)
        session.commit()
