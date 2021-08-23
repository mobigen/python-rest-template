from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.common.config import SqliteConf

sqlite_conf = SqliteConf()

SQLALCHEMY_DATABASE_URL = f'sqlite:///{sqlite_conf.path}/{sqlite_conf.file_name}'

Base = declarative_base()


class Sqlite:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Sqlite().__instance
        return cls.__instance

    def __init__(self):
        if Sqlite.__instance is None:
            Sqlite.__instance = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

    def __enter__(self):
        session = sessionmaker(autocommit=False, autoflush=False, bind=Sqlite.get_instance())
        self.session = session()
        return self.session

    def __exit__(self, *args):
        self.session.close()



