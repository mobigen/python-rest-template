import redis

from app.common.config import RedisConf

redis_conf = RedisConf()

rcline = redis.Redis(host=redis_conf.host, port=redis_conf.port, password=redis_conf.password)


