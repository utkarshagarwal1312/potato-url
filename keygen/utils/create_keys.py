import string
import logging
from random import random
import redis
from keygen.models import Key
from potato_url.settings import REDIS_POOL

cache = redis.Redis(connection_pool=REDIS_POOL)

logger = logging.getLogger(__name__)


class KeyPoolGenerator:
    def __init__(self, number_of_keys=1000):
        self.number_of_keys = number_of_keys

    @staticmethod
    def _random_string_generator(str_size=6, allowed_chars=string.ascii_letters + '0123456789'):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))

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
                count += 1
                key = self._random_string_generator()
            else:
                return key

    def _generate_keys(self):
        generated_keys = []
        for i in range(self.number_of_keys):
            unique_key = self._generate_unique_key()
            if not unique_key:
                break
            generated_keys.append(Key(val=unique_key))
        if generated_keys:
            Key.objects.bulk_create(generated_keys, batch_size=len(generated_keys), ignore_conflicts=True)
            return len(generated_keys)
        return 0

    def generate(self):
        number_of_keys_generated = self._generate_keys()
        if number_of_keys_generated < self.number_of_keys:
            logger.exception("Key Generation could not create required keys.")
