from django.test import TestCase

from keygen.models import Key
from keygen.utils.key_pool import KeyPoolGenerator


# Create your tests here.
class UtilsTest(TestCase):
    # TODO : Add redis for test, or use different set for test
    def test_util_key_pool_generator(self):
        KeyPoolGenerator(number_of_keys=100).generate_keys()
        self.assertEqual(Key.objects.filter(is_used=False).count(), 80)

    def test_util_key_pool_generator_for_1(self):
        KeyPoolGenerator(number_of_keys=1).generate_keys()
        self.assertEqual(Key.objects.filter(is_used=True).count(), 1)
