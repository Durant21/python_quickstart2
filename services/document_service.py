from typing import List, Optional

import data.db_session as db_session
from Domain.Documents import Document


def get_all_documents(limit=10) -> List[Document]:
    session = db_session.create_session()

    docs = session.query(Document).all()

    session.close()

    return docs


def get_document_by_name(doc_name: str) -> Optional[Document]:
        session = db_session.create_session()
        doc_name = '35'
        doc = session.query(Document).filter(Document.doc_name == doc_name).first()
        return doc


def get_document_by_id(doc_id: str) -> Optional[Document]:
    session = db_session.create_session()
    doc = session.query(Document).filter(Document.doc_id == doc_id).first()
    return doc


def create_document(doc_name: str) -> Optional[Document]:
    # if find_document_by_title(document):
    #     return None

    doc = Document()
    doc.doc_name = doc_name

    session = db_session.create_session()
    session.add(doc)
    session.commit()

    return doc