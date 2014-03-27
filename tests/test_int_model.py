import unittest

from django.conf import settings
if not settings.configured:
    settings.configure(DEBUG=True)
from django.db import models

from django_mothers import Mother


class Example(models.Model):
    field_1 = models.IntegerField()
    field_2 = models.IntegerField()


class TestIntegerFields(unittest.TestCase):
    def test_create_integer_mother(self):
        mother = Mother(Example)

        self.assertIsInstance(mother.field_1, int)
        self.assertIsInstance(mother.field_2, int)
        self.assertGreaterEqual(mother.field_1, -2147483648)
        self.assertLessEqual(mother.field_1, 2147483647)

    def test_create_using_my_own_data(self):
        mother = Mother(Example, field_1=3)

        self.assertEquals(3, mother.field_1)
