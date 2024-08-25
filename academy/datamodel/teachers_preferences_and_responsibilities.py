from .model_base import SqlAlchemyBase

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Teachers_pref_resp(SqlAlchemyBase):
    __tablename__ = 'teachers_preferences_and_responsibilities'

    id: Mapped[int] = mapped_column(primary_key=True)
    preference_id_for_teachers: Mapped[int] = mapped_column(ForeignKey('teachers.id'), unique=True)
    day_for_working: Mapped[str] = mapped_column(nullable=False)
    time_for_working: Mapped[str] = mapped_column(nullable=False)
    language_to_speak: Mapped[str] = mapped_column(nullable=False)
    age_for_training: Mapped[str] = mapped_column(nullable=True)
    number_of_trainees: Mapped[int] = mapped_column(nullable=False)


    def __repr__(self):
        return f'Teachers_pref_resp(id = {self.id}, preference_id_for_teachers = {self.preference_id_for_teachers},\n\
        day_for_working = {self.day_for_working}, time_for_working = {self.time_for_working},\n\
        language_to_speak = {self.language_to_speak}, age_for_training = {self.age_for_training},\n\
        number_of_trainees = {self.number_of_trainees})\n'
