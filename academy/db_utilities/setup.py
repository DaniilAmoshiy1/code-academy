from academy.datamodel.model_base import SqlAlchemyBase
from .session import AcademySession


def reset_db():
    SqlAlchemyBase.metadata.drop_all(AcademySession.engine)


def setup_db():
    SqlAlchemyBase.metadata.create_all(AcademySession.engine)
