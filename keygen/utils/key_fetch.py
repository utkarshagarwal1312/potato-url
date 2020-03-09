from keygen.models import Key
from keygen.utils.key_pool import KeyPoolGenerator
from potato_url.settings import REDIS
from keygen.constants import IN_MEMORY_KEY_POOL_SET


def fetch_key():
    key = REDIS.spop(IN_MEMORY_KEY_POOL_SET, 1)
    if not key:
        generation_error = KeyPoolGenerator(number_of_keys=1).generate_keys()
        if not generation_error:
            key = REDIS.spop(IN_MEMORY_KEY_POOL_SET, 1)
    # TODO :
    #  1. Call async for default KeyPoolGeneration
    #  2. Call async for shifting ratio of is_used=False to Memory

    return Key.objects.get(val=key[0].decode("utf-8"))
