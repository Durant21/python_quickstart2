import sys
import csv
import os
import random

from dateutil.parser import parse

from data.db_factory import DbSessionFactory
from Domain.Doc_Parent import DocumentParent
from Domain.Documents import Document
from Domain.Documents import Document

class DAL_Doc_Parent:
    __section_data = {}
    #
    # @classmethod
    # def all_sections(cls,limit=None):
    #     session = DbSessionFactory.create_session()
    #     query = session.query(Section)
    #
    #     if limit:
    #         sections = query[:limit]
    #     else:
    #         sections = query.all()
    #
    #     session.close()
    #
    #     return sections
    #
    #
    @classmethod
    def doc_parent_by_doc_id(cls, doc_id):
        session = DbSessionFactory.create_session()
        # section = session.query(Section).filter(Section.sec_id == sec_id).first()
        u = 0;
        docs = []
        # for dp, d1a, d2a in session.query(DocumentParent, d1, d2).\
        #         filter(DocumentParent.doc_id == d1.doc_id,\
        #                DocumentParent.parent_id == d2.doc_id).all():
        #                # d2.doc_id == doc_id).all():

        # for dp, d1a, d2a in session.query(DocumentParent, d1, d2). \
        #         filter(DocumentParent.doc_id == d1.doc_id,\
        #                DocumentParent.parent_id == d2.doc_id).all():
        q = (session.query(DocumentParent, Document,Document)
             .filter(DocumentParent.doc_id == Document.doc_id)
             .filter(DocumentParent.parent_id == Document.doc_id)
             # .filter(User.email == 'someemail')
             .all())

        u = u + 1

        # print("relationship: {} doc_name: {} doc_name: {}".format(dp.relationship, d1a.doc_name))
        print("relationship: {} doc_name: {} doc_name: {}".format(DocumentParent.relationship, d1.doc_name, d2.doc_name))
            #
            # u = Doc_Group_Sec()
            #
            # u.add_group_id(g.group_id)
            # u.add_doc_name(d.doc_name)
            # u.add_sec_text(s.sec_text)
            # u.add_sec_id(s.sec_id)
            #
            # docs.append(u.to_dict())



        session.close()

        return u # docs
    #
    # @classmethod
    # def section_by_doc(cls, doc_id):
    #     session = DbSessionFactory.create_session()
    #     section = session.query(Group).filter(Group.doc_id == doc_id).all()
    #     session.close()
    #
    #     return section

    @classmethod
    def create_doc_parent(cls,doc_parent):
        try:
            session = DbSessionFactory.create_session()

            db_doc_parent = DocumentParent()
            # db_doc_parent.doc_parent_id = doc_parent['doc_parent_id']
            db_doc_parent.doc_id = doc_parent['doc_id']
            db_doc_parent.parent_id = doc_parent['parent_id']
            db_doc_parent.relationship = doc_parent['relationship']

            session.add(db_doc_parent)
            session.commit()

            return db_doc_parent

        except Exception as e:
            print (e)
