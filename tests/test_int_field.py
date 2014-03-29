import sys
if sys.version_info < (3, 0):
    import unittest2 as unittest
else:
    import unittest

from django.db import models

from django_mothers import Mother


class IntegerExample(models.Model):
    field_1 = models.IntegerField()
    field_2 = models.IntegerField()


class TestIntegerFields(unittest.TestCase):
    def test_create_integer_mother(self):
        mother = Mother(IntegerExample)

        self.assertIsInstance(mother.field_1, int)
        self.assertIsInstance(mother.field_2, int)
        self.assertGreaterEqual(mother.field_1, -2147483648)
        self.assertLessEqual(mother.field_1, 2147483647)

    def test_create_using_my_own_data(self):
        mother = Mother(IntegerExample, field_1=3)

        self.assertEquals(3, mother.field_1)

    def test_create_using_generator(self):
        def generator(field_name):
            return 9

        mother = Mother(IntegerExample, field_1=generator)

        self.assertEqual(9, mother.field_1)
