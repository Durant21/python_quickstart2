import sys
import csv
import os
import random

from dateutil.parser import parse
import data.db_session as db_session
from data.db_factory import DbSessionFactory
from Domain.Sections import Section
from Domain.Groups import Group

class DAL_Sections:
    __section_data = {}

    @classmethod
    def all_sections(cls,limit=None):
        session = db_session.create_session()
        # session = DbSessionFactory.create_session()
        query = session.query(Section)

        if limit:
            sections = query[:limit]
        else:
            sections = query.all()

        session.close()

        return sections

    @classmethod
    def section_by_id(cls, sec_id):
        session = db_session.create_session()
        # session = DbSessionFactory.create_session()
        section = session.query(Section).filter(Section.sec_id == sec_id).first()
        session.close()

        return section

    @classmethod
    def section_by_doc(cls, doc_id):
        # session = db_session.create_session()
        session = DbSessionFactory.create_session()
        section = session.query(Group).filter(Group.doc_id == doc_id).all()
        session.close()

        return section

    @classmethod
    def add_section(cls,section):
        try:
            session = db_session.create_session()
            # session = DbSessionFactory.create_session()

            db_section = Section()
            # db_section.sec_id = section.sec_id
            db_section.sec_text = section.sec_text
            db_section.sec_date_in = parse(section.sec_date_in)

            session.add(db_section)
            session.commit()

            return db_section

        except Exception as e:
            print (e)

    @classmethod
    def update_section(cls, section_data):
        try:
            session = db_session.create_session()

            db_section = session.query(Section).filter(Section.sec_id == section_data.sec_id).first()
            db_section.sec_text = section_data.sec_text
            db_section.sec_date_in = parse(section_data.sec_date_in)

            session.commit()

            return db_section
        except Exception as e:
            print(e)


    @classmethod
    def delete_section(cls, sec_id):
        session = db_session.create_session()
        db_section = session.query(Section).filter(Section.sec_id == sec_id).first()

        if not db_section:
            return

        session.delete(sec_id)
        session.commit()


