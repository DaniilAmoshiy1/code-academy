from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from academy.datamodel.model_base import SqlAlchemyBase


class Staff(SqlAlchemyBase):
    __tablename__ = 'staff'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    age: Mapped[int] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=True)
    speciality: Mapped[str] = mapped_column(nullable=False)
    work_mail: Mapped[str] = mapped_column(nullable=True)
    birthday: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    start_work: Mapped[DateTime] = mapped_column(DateTime, default=datetime(2024, 1, 1))
    salary: Mapped[int] = mapped_column(nullable=False)


    def __repr__(self):
        return f'Staff(id = {self.id}, name = {self.name}, age = {self.age}, gender = {self.gender}\n\
        speciality = {self.speciality}, work_mail = {self.work_mail}, birthday = {self.birthday}\n\
        start_work = {self.start_work}, salary = {self.salary})\n'
