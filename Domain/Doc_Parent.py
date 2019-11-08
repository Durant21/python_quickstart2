import uuid
import sqlalchemy
import datetime

from data.sqlalchemy_base import SqlAlchemyBase


class DocumentParent(SqlAlchemyBase):
    __tablename__ = 'Document_Parent'

    doc_parent_id = sqlalchemy.Column(sqlalchemy.String,primary_key=True,
                               default=lambda: str(uuid.uuid4()))
    doc_id = sqlalchemy.Column(sqlalchemy.String)
    parent_id = sqlalchemy.Column(sqlalchemy.String)
    relationship = sqlalchemy.Column(sqlalchemy.String) # direct/copy

    def to_dict(self):
        return {
            'doc_parent_id': self.doc_parent_id,
            'doc_id': self.doc_id,
            'parent_id': self.parent_id,
            'relationship': self.relationship,
        }