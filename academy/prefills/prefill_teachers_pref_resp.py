from academy.datamodel.teachers_preferences_and_responsibilities import Teachers_pref_resp
from academy.db_utilities.session import AcademySession


def prefill_teachers_pref_resp():
    with AcademySession.get_session() as session:
        teachers_pref_data = [
            Teachers_pref_resp(
                preference_id_for_teachers=1,
                day_for_working='Tuesday, Saturday',
                time_for_working='Tuesday: 19:00 - 22:00, Saturday: 12:00 - 15:00',
                language_to_speak='Russian, English',
                number_of_trainees=7
            ),
            Teachers_pref_resp(
                preference_id_for_teachers=2,
                day_for_working='Wednesday, Friday, Sunday',
                time_for_working='Wednesday: 14:00 - 16:00, Friday: 17:00 - 19:00, Sunday: 9:00 - 11:00',
                language_to_speak='Russian',
                number_of_trainees=6
            ),
            Teachers_pref_resp(
                preference_id_for_teachers=3,
                day_for_working='Monday, Tuesday',
                time_for_working='Monday: 11:00 - 14:00, Tuesday: 14:00 - 17:00',
                language_to_speak='Russian, English',
                age_for_training='14-40',
                number_of_trainees=8
            ),
            Teachers_pref_resp(
                preference_id_for_teachers=4,
                day_for_working='Friday, Sunday',
                time_for_working='Friday: 13:00 - 16:00, Sunday: 16:00 - 19:00',
                language_to_speak='English, French',
                age_for_training='18-70',
                number_of_trainees=9
            ),
            Teachers_pref_resp(
                preference_id_for_teachers=5,
                day_for_working='Wednesday, Friday',
                time_for_working='Wednesday: 12:30 - 16:00, Friday: 17:00 - 20:00',
                language_to_speak='Russian',
                number_of_trainees=4
            ),
            Teachers_pref_resp(
                preference_id_for_teachers=6,
                day_for_working='Monday - Friday',
                time_for_working='All: 10:00 - 12:00',
                language_to_speak='Russian, English',
                number_of_trainees=5
            ),
            Teachers_pref_resp(
                preference_id_for_teachers=7,
                day_for_working='Friday - Sunday',
                time_for_working='All: 16:00 - 18:00',
                language_to_speak='English',
                age_for_training='15-40',
                number_of_trainees=7
            ),
            Teachers_pref_resp(
                preference_id_for_teachers=8,
                day_for_working='Thursday, Saturday',
                time_for_working='All: 18:00 - 21:00',
                language_to_speak='Russian, English',
                number_of_trainees=9
            )
        ]
        session.add_all(teachers_pref_data)
        session.commit()
