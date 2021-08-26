import logging
from app.config import Config


log_level = Config.log.level.upper()
log_format = "[%(asctime)s] %(levelname)s, %(process)s-%(thread)d, %(filename)s(%(lineno)d), %(message)s"
formatter = logging.Formatter(log_format)

"""
uvicorn 을 위한 log config
uvicorn 에서 사용되는 구조를 이용
"""
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": log_format,
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "[%(asctime)s] %(levelname)s, %(process)s-%(thread)d, %(message)s",
            "use_colors": None,
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": log_level, "propagate": False},
        "uvicorn.error": {"handlers": ["default"], "level": log_level, "propagate": False},
        "uvicorn.access": {"handlers": ["access"], "level": log_level, "propagate": False},
    },
}


def setup_logger(handler_name=None):
    """
    default logger 설정
    코드상에서 사용될 로그
    """
    if handler_name is None:
        log = logging.getLogger()
    else:
        log = logging.getLogger(handler_name)

    if log_level.lower() == 'error':
        log.setLevel(logging.ERROR)
    elif log_level.lower() == 'debug':
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

    log.propagate = False

    log.handlers.clear()
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)


setup_logger()
