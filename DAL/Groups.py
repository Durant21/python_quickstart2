import sys
import csv
import os
import random

from dateutil.parser import parse

# from data.db_factory import DbSessionFactory
import data.db_session as db_session
from Domain.Groups import Group
from Domain.Sections import Section
from Domain.Documents import Document
from Domain.Doc_Group_Sec import Doc_Group_Sec

class DAL_Groups:
    __group_data = {}

    @classmethod
    def all_groups(cls,limit=None):
        session = db_session.create_session()
        query = session.query(Group)

        if limit:
            groups = query[:limit]
        else:
            groups = query.all()

        session.close()

        return groups

    @classmethod
    def get_documents_sections(cls,doc_id,limit=None):
        session = db_session.create_session()
        # query = session.query(Group)
        docs = []
        for d, g, s in session.query(Document, Group, Section).\
                filter(Document.doc_id == Group.doc_id,\
                       Section.sec_id == Group.sec_id,\
                       Document.doc_id == doc_id).all():
            print("group_id: {} doc_name: {}  text: {}".format(g.group_id, d.doc_name, s.sec_text))

            u = Doc_Group_Sec()

            u.add_group_id(g.group_id)
            u.add_doc_name(d.doc_name)
            u.add_doc_id(d.doc_id)
            u.add_sec_text(s.sec_text)
            u.add_sec_id(s.sec_id)
            u.add_order(g.order)

            docs.append(u.to_dict())


        # docs = session.quget_sections_by_docery(Document, Group, Section).\
        #     filter(Document.doc_id == Group.doc_id,\
        #            Section.sec_id == Group.sec_id, \
        #             Document.doc_id == doc_id).all()
        # if limit:
        #     groups = query[:limit]
        # else:
        #     groups = query.all()

        session.close()

        return docs


    @classmethod
    def get_documents_sections_to_obj(cls,doc_id,limit=None):
        session = db_session.create_session()
        # query = session.query(Group)
        docs = []
        for d, g, s in session.query(Document, Group, Section).\
                filter(Document.doc_id == Group.doc_id,\
                       Section.sec_id == Group.sec_id,\
                       Document.doc_id == doc_id).all():
            print("group_id: {} doc_name: {}  text: {}".format(g.group_id, d.doc_name, s.sec_text))

            u = Doc_Group_Sec()

            u.add_group_id(g.group_id)
            u.add_doc_name(d.doc_name)
            u.add_doc_id(d.doc_id)
            u.add_sec_text(s.sec_text)
            u.add_sec_id(s.sec_id)
            u.add_order(g.order)

            docs.append(u)


        # docs = session.query(Document, Group, Section).\
        #     filter(Document.doc_id == Group.doc_id,\
        #            Section.sec_id == Group.sec_id, \
        #             Document.doc_id == doc_id).all()
        # if limit:
        #     groups = query[:limit]
        # else:
        #     groups = query.all()

        session.close()

        return docs



    @classmethod
    def group_by_id(cls, group_id):
        session = db_session.create_session()
        group = session.query(Group).filter(Group.group_id == group_id).first()
        session.close()

        return group

    @classmethod
    def add_group(cls,group):
        try:
            session = db_session.create_session()

            db_group = Group()
            # db_section.sec_id = section.sec_id
            db_group.doc_id = group.doc_id
            db_group.sec_id = group.sec_id
            db_group.order = 1

            session.add(db_group)
            session.commit()

            return db_group

        except Exception as e:
            print (e)

    @classmethod
    def update_group(cls, group_data):
        try:
            session = db_session.create_session()

            db_group = session.query(Group).filter(Group.group_id == group_data.group_id).first()
            db_group.doc_id = group_data.doc_id
            db_group.sec_id = group_data.sec_id

            session.commit()

            return db_group
        except Exception as e:
            print(e)


    @classmethod
    def delete_group(cls, group_id):
        session = db_session.create_session()
        db_group = session.query(Group).filter(Group.group_id == group_id).first()

        if not db_group:
            return

        session.delete(group_id)
        session.commit()


