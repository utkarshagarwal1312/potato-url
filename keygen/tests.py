from django.test import TestCase

from keygen.models import Key
from keygen.utils.key_pool import KeyPoolGenerator


# Create your tests here.
class UtilsTest(TestCase):
    def test_util_key_pool_generator(self):
        KeyPoolGenerator(number_of_keys=100).generate_keys()
        self.assertEqual(Key.objects.all().count(), 100)
