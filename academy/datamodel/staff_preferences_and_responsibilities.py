from sqlalchemy import  ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from academy.datamodel.model_base import SqlAlchemyBase


class Staff_pref_resp(SqlAlchemyBase):
    __tablename__ = 'staff_preferences_and_responsibilities'

    id: Mapped[int] = mapped_column(primary_key=True)
    staff_id: Mapped[int] = mapped_column(ForeignKey('staff.id'), unique=True)
    time_for_working: Mapped[str] = mapped_column()
    day_for_working: Mapped[str] = mapped_column()
    language_to_speak: Mapped[str] = mapped_column()
