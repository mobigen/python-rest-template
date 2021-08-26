from app.config.base_config import BaseConfig
from app.error.exceptions import ConfigException


class _Server:
    host = "127.0.0.1"
    port = 9999
    workers = 1
    logging = "aaa"


class _Log:
    level = "INFO"

    def validation_check(self):
        self.level = self.level.upper()
        if self.level.lower() not in ['info', 'debug', 'error']:
            raise ConfigException('log.level', self.level, 'not used value')


class _Database:
    class _Redis:
        host = "0.0.0.0"
        port = "3000"
        password = "aaaaaa"

    redis = _Redis()


class Config(BaseConfig):
    server = _Server()
    log = _Log()
    database = _Database()


if __name__ == '__main__':
    Config.init('/Users/anhm/Dev/mobigen/python-rest-template/conf/fast_api_conf_template.yaml')
    print(Config.server.host)
    print(Config.log.level)
    print(Config.database)
