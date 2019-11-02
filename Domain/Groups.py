import uuid
import sqlalchemy
from data.modelbase import SqlAlchemyBase


class Group(SqlAlchemyBase):
    __tablename__ = 'Groups'

    group_id = sqlalchemy.Column(sqlalchemy.String,primary_key=True,
                               default=lambda: str(uuid.uuid4()))
    doc_id = sqlalchemy.Column(sqlalchemy.String)
    sec_id = sqlalchemy.Column(sqlalchemy.String)
    order = sqlalchemy.Column(sqlalchemy.String)

    def to_dict(self):
        return {
            'group_id': self.group_id,
            'doc_id': self.doc_id,
            'sec_id': self.sec_id,
            'order': self.order,
        }
