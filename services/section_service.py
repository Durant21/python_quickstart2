from typing import List
from dateutil.parser import parse
import data.db_session as db_session
from Domain.Sections import Section


def get_all_sections(limit=10) -> List[Section]:
    session = db_session.create_session()

    docs = session.query(Section).all()

    session.close()

    return docs


def add_section(cls,section):
        try:
            session = db_session.create_session()

            db_section = Section()
            db_section.sec_text = section.sec_text
            db_section.sec_date_in = parse(section.sec_date_in)

            session.add(db_section)
            session.commit()

            return db_section

        except Exception as e:
            print (e)