from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from academy.datamodel.model_base import SqlAlchemyBase


class Students(SqlAlchemyBase):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    subject: Mapped[str] = mapped_column(nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'), nullable=False)


    def __repr__(self):
        return f'Students(id = {self.id}, name = {self.name}, age = {self.age}\n\
        subject = {self.subject}, teacher_id = {self.teacher_id})\n'
