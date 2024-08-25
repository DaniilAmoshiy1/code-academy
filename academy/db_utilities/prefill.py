from academy.prefills import prefill_staff
from academy.prefills import prefill_staff_pref_resp
from academy.prefills import prefill_teachers
from academy.prefills import prefill_teachers_pref_resp
from academy.prefills import prefill_students


def prefill_database():
    prefill_staff()
    prefill_staff_pref_resp()
    prefill_teachers()
    prefill_teachers_pref_resp()
    prefill_students()
