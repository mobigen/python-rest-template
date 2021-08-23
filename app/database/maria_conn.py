from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.common.config import MariaConf

maria_conf = MariaConf()

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(maria_conf.user, maria_conf.password, maria_conf.host, maria_conf.port, maria_conf.dbname)

Base = declarative_base()


class Maria:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Maria().__instance
        return cls.__instance

    def __init__(self):
        if Maria.__instance is None:
            Maria.__instance = create_engine(SQLALCHEMY_DATABASE_URL, echo=False, encoding='utf8', pool_recycle=3600, pool_pre_ping=True)

    def __enter__(self):
        session = sessionmaker(autocommit=False, autoflush=False, bind=Maria.get_instance())
        self.session = session()
        return self.session

    def __exit__(self, *args):
        self.session.close()



