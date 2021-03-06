import sys
if sys.version_info < (3, 0):
    import unittest2 as unittest
else:
    import unittest

from django.db import models

from orm_mothers import DjangoMother as Mother


class BooleanExample(models.Model):
    field_1 = models.BooleanField()
    field_2 = models.BooleanField()


class TestBooleanFields(unittest.TestCase):
    def test_create_boolean_mother(self):
        mother = Mother(BooleanExample)

        self.assertIsInstance(mother.field_1, bool)
        self.assertIsInstance(mother.field_2, bool)

    def test_create_using_my_own_data(self):
        mother = Mother(BooleanExample, field_1=True, field_2=False)

        self.assertTrue(mother.field_1)
        self.assertFalse(mother.field_2)
