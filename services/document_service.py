from typing import List, Optional
import sqlalchemy.orm

import data.db_session as db_session
from data.Documents import Document


def get_all_documents(limit=10) -> List[Document]:
    session = db_session.create_session()

    docs = session.query(Document).all()

    session.close()

    return docs
