import os
import yaml

from app.error.exceptions import FastException


class Config(object):
    """
    기본 Configuration
    """
    CONFIG_FILE_PATH = None

    try:
        with open('/Users/jheok/Desktop/fast_template/app/conf/fast_api_conf_template.yaml') as fd:
            CONFIG_FILE_PATH = yaml.load(fd, Loader=yaml.FullLoader)
    except Exception:
        FastException('Please set retry config file')

    def __init__(self):
        self.config = Config.CONFIG_FILE_PATH


class ServerConf(Config):

    def __init__(self):
        super(ServerConf, self).__init__()
        server = self.config.get("server")
        self.host: str = server.get("host")
        self.port: int = server.get("port")

    def as_dict(self):
        return {"host": self.host, "port": self.port}


class RedisConf(Config):

    def __init__(self, ):
        super(RedisConf, self).__init__()
        database = self.config.get("database")
        redis_conf = database.get("redis")
        self.host: str = redis_conf.get("host")
        self.port: int = redis_conf.get("port")
        self.password: int = redis_conf.get("password")

    def as_dict(self):
        return {"host": self.host, "port": self.port}


class MariaConf(Config):

    def __init__(self, ):
        super(MariaConf, self).__init__()
        database = self.config.get("database")
        mysql_conf = database.get("maria")
        self.user: str = mysql_conf.get("user")
        self.host: str = mysql_conf.get("host")
        self.port: int = mysql_conf.get("port")
        self.password: int = mysql_conf.get("password")
        self.dbname: int = mysql_conf.get("dbname")

    def as_dict(self):
        return {"user": self.user, "host": self.host, "port": self.port, "password": self.password, "dbname": self.dbname}


class SqliteConf(Config):

    def __init__(self, ):
        super(SqliteConf, self).__init__()
        database = self.config.get("database")
        mysql_conf = database.get("sqlite")
        self.path: str = mysql_conf.get("path")
        self.file_name: int = mysql_conf.get("file_name")

    def as_dict(self):
        return {"path": self.path, "file_name": self.file_name}


class LogConf(Config):

    def __init__(self, ):
        super(LogConf, self).__init__()
        self.log_file: str = self.config.get("log_file")

    def as_dict(self):
        return {"log_file": self.log_file}


class SimpleAngoraConf(Config):

    def __init__(self, ):
        super(SimpleAngoraConf, self).__init__()
        s_angora_conf = self.config.get("simple_angora")
        self.host: str = s_angora_conf.get("host")
        self.port: str = s_angora_conf.get("port")
        self.user: str = s_angora_conf.get("user")
        self.password: str = s_angora_conf.get("password")

    def as_dict(self):
        return {"host": self.host, "port": self.port, "user": self.user, "password": self.password}
