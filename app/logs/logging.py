import logging
config = {}
config['log_config'] = {
            'version': 1, 'disable_existing_loggers': True,
            'formatters': {'default': {'()': 'uvicorn.logging.DefaultFormatter', 'fmt': '%(levelprefix)s %(message)s', 'use_colors': None},
                           'access': {'()': 'uvicorn.logging.AccessFormatter', 'fmt': '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'}},
            'handlers': {'default': {'formatter': 'default', 'class': 'logging.StreamHandler', 'stream': 'ext://sys.stderr'},
                         'access': {'formatter': 'access', 'class': 'logging.StreamHandler', 'stream': 'ext://sys.stdout'}},
            'loggers': {'uvicorn': {'handlers': ['default'], 'level': 'INFO'},
                        'uvicorn.error': {'level': 'INFO', 'handlers': ['default'], 'propagate': True},
                        'uvicorn.access': {'handlers': ['access'], 'level': 'INFO', 'propagate': False},
                        },
        }

# add your handler to it (in my case, I'm working with quart, but you can do this with Flask etc. as well, they're all the same)
# config['log_config']['loggers']['quart'] = {'handlers': ['default'], 'level': 'INFO'}



class FastLogger(object):
    _log = None

    def __init__(self):
        self._log = logging.getLogger('uvicorn.error')
        self._log.setLevel(logging.INFO)
        self._log.propagate = False

        self._log2 = logging.getLogger('uvicorn.access')
        self._log2.propagate = False

        log_format = f"[%(asctime)s] %(levelname)s, file %(filename)s, " \
                     f"line %(lineno)d, %(message)s"

        formatter = logging.Formatter(log_format, '%Y/%m/%d %H:%M:%S')

        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        self._log.addHandler(streamHandler)
        # self._log.propagate = False

        # logger = logging.getLogger("uvicorn.access")
        # handler = logging.StreamHandler()
        # handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        # logger.addHandler(handler)

        # <file log skeleton>

        # import datetime
        # import time
        # now = datetime.datetime.now()
        # timestamp = time.mktime(now.timetuple())
        #
        # dirname = './log'
        # if not os.path.isdir(dirname):
        #     os.mkdir(dirname)
        # fileHandler = logging.FileHandler(dirname + "/Aries_" + now.strftime("%Y-%m-%d %H:%M:%S") + ".log")
        # fileHandler.setFormatter(formatter)
        # self._log.addHandler(fileHandler)