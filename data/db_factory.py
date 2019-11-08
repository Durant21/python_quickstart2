import os
import sqlalchemy
import sqlalchemy.orm

# code from DocTrace_v3
from data.sqlalchemy_base import SqlAlchemyBase


class DbSessionFactory:
    __session_factory = None

    @classmethod
    def global_init(cls, db_filename):
        ww = os.path.dirname(os.path.abspath(__file__))
        working_folder = os.path.dirname(ww)
        # working_folder = os.path.dirname(placeholder.txt.__file__)
        file = os.path.join(working_folder,'db',db_filename)
        conn_string = 'sqlite:///' + file

        # print("conn : " + conn_string)
        engine = sqlalchemy.create_engine(conn_string,echo=True)
        # engine = sqlalchemy.create_engine(conn_string,echo=True)

        SqlAlchemyBase.metadata.create_all(engine)

        cls.__session_factory  = sqlalchemy.orm.sessionmaker(bind=engine)

    @classmethod
    def create_session(cls):
        return cls.__session_factory()





