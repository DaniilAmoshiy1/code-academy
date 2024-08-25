from datetime import datetime
import random

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from academy.datamodel.model_base import SqlAlchemyBase


class Teachers(SqlAlchemyBase):
    __tablename__ = 'teachers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column()
    birthday: Mapped[DateTime] = mapped_column(DateTime, default=datetime)
    salary: Mapped[int] = mapped_column(default=5000, nullable=False)
    work_experience_in_years: Mapped[int] = mapped_column(default=0)
    speciality: Mapped[str] = mapped_column(nullable=True, default=None)
    language_for_programming: Mapped[str] = mapped_column(nullable=True, default=None)
    rating: Mapped[float] = mapped_column(default=round(random.uniform(2.5, 5.0), 1))


    def __repr__(self):
        return f'Teachers(id = {self.id}, name = {self.name}, age = {self.age},\n\
        gender = {self.gender}, birthday = {self.birthday}, salary = {self.salary},\n\
        work_experience_in_years = {self.work_experience_in_years}, speciality = {self.speciality}, \n\
        language_for_programming = {self.language_for_programming}, rating = {self.rating})\n'
