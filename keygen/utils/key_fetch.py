import redis

from keygen.models import Key
from potato_url.settings import REDIS_POOL

cache = redis.Redis(connection_pool=REDIS_POOL)
