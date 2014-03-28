try:
    import unittest2 as unittest
except ImportError:
    import unittest

from django.db import models

from django_mothers import Mother


class Example(models.Model):
    field_1 = models.BigIntegerField()
    field_2 = models.BigIntegerField()


class TestBigIntegerFields(unittest.TestCase):
    def test_create_integer_mother(self):
        mother = Mother(Example)

        self.assertIsInstance(mother.field_1, int)
        self.assertIsInstance(mother.field_2, int)

    def test_create_using_my_own_data(self):
        mother = Mother(Example, field_1=214748364856)

        self.assertEquals(214748364856, mother.field_1)
