import uuid
import sqlalchemy
import datetime

from data.sqlalchemy_base import SqlAlchemyBase

class Section(SqlAlchemyBase):
    __tablename__ = 'Sections'

    sec_id = sqlalchemy.Column(sqlalchemy.String,primary_key=True,
                               default=lambda: str(uuid.uuid4()))
    sec_text = sqlalchemy.Column(sqlalchemy.String)
    sec_date_in = sqlalchemy.Column(sqlalchemy.DATE, index=True)

    def to_dict(self):
        return {
            'sec_id': self.sec_id,
            'sec_text': self.sec_text,
            'sec_date_in': self.sec_date_in.isoformat(),
        }
