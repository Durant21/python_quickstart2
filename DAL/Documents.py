import sys
import csv
import os
import random

from dateutil.parser import parse
import data.db_session as db_session
# from data.db_factory import DbSessionFactory
from Domain.Documents import Document

class DAL_Documents:
    __document_data = {}

    @classmethod
    def all_documents(cls,limit=None):
        session = db_session.create_session()
        query = session.query(Document). \
            order_by(Document.doc_name)

        if limit:
            documents = query[:limit]
        else:
            documents = query.all()

        session.close()

        return documents


    @classmethod
    def doc_by_id(cls, doc_id):
        session = db_session.create_session()
        document = session.query(Document).filter(Document.doc_id == doc_id).first()
        session.close()

        return document


    @classmethod
    def doc_by_name(cls, doc_name):
        session = db_session.create_session()
        document = session.query(Document).filter(Document.doc_name == doc_name).first()
        session.close()

        return document

    @classmethod
    def add_document(cls, doc):
        try:
            session = db_session.create_session()

            db_doc = Document()
            db_doc.doc_id = doc.doc_id
            db_doc.doc_name = doc.doc_name

            session.add(db_doc)
            session.commit()

            return db_doc

        except Exception as e:
            print (e)

    @classmethod
    def update_document(cls, doc_data):
        session = db_session.create_session()

        db_doc = session.query(Document).filter(Document.doc_id == doc_data.doc_id).first()
        db_doc.doc_name = doc_data.doc_name

        session.commit()

        return db_doc


    @classmethod
    def delete_document(cls, doc_id):
        session = db_session.create_session()
        db_doc = session.query(Document).filter(Document.doc_id == doc_id).first()

        if not db_doc:
            return

        session.delete(doc_id)
        session.commit()


