from academy.config import PRINT_ITEMS_PER_PAGE
from academy.db_utilities.session import AcademySession


def get_recent_entries(model_object, page=1, limit=PRINT_ITEMS_PER_PAGE):
    offset = (page - 1) * limit
    with AcademySession.get_session() as session:
        query = session.query(model_object).order_by(model_object.id.asc())
        if limit:
            query = query.limit(limit).offset(offset)
        data = query.all()
    return data
