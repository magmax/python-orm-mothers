import sys
if sys.version_info < (3, 0):
    import unittest2 as unittest
else:
    import unittest

from django.db import models

from orm_mothers import DjangoMother as Mother


class StringExample(models.Model):
    field_1 = models.CharField(max_length=10)
    field_2 = models.CharField()


class TestCharFields(unittest.TestCase):
    def test_create_string_mother(self):
        mother = Mother(StringExample)

        self.assertIsInstance(mother.field_1, str)
        self.assertIsInstance(mother.field_2, str)

    def test_use_fixed_data(self):
        mother = Mother(StringExample, field_2='fulanito')

        self.assertEqual(mother.field_2, 'fulanito')
