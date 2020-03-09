import string
import logging

import random
import redis
from keygen.models import Key
from potato_url.settings import REDIS_POOL

cache = redis.Redis(connection_pool=REDIS_POOL)

logger = logging.getLogger(__name__)


class KeyPoolGenerator:
    # TODO :
    #  1. Find a better way to generate keys such that Key obj(id=k) and Key obj(id=k+1) have no
    #  direct relationship.
    #  2. Add bulk create for keys

    def __init__(self, number_of_keys=1000):
        self.number_of_keys = number_of_keys
        self.same_key_generated = False

    @staticmethod
    def _random_string_generator(str_size=6, allowed_chars=string.ascii_letters + '0123456789'):
        key = ''.join(random.choice(allowed_chars) for x in range(str_size))
        return key

    @staticmethod
    def _check_key_already_exists(key):
        return Key.objects.filter(val=key).exists()

    def _generate_unique_key(self):
        key = self._random_string_generator()
        count = 0
        while True:
            if count > 1000:
                return None
            elif self._check_key_already_exists(key):
                self.same_key_generated = True
                count += 1
                key = self._random_string_generator()
            else:
                Key.objects.create(val=key)
                return key

    def generate_keys(self):
        generation_error = True
        for i in range(self.number_of_keys):
            unique_key = self._generate_unique_key()
            if not unique_key:
                break
        else:
            generation_error = False

        if generation_error:
            logger.exception("Key Generation could not create required keys.")
