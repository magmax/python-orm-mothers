import sys
if sys.version < (3, 0):
    import unittest2 as unittest
else:
    import unittest

from django.db import models

from django_mothers import Mother


class CSIExample(models.Model):
    field_1 = models.CommaSeparatedIntegerField()
    field_2 = models.CommaSeparatedIntegerField()


class TestCSIFields(unittest.TestCase):
    def test_create_boolean_mother(self):
        mother = Mother(CSIExample)

        self.assertIsInstance(mother.field_1, str)
        self.assertIsInstance(mother.field_2, str)

    def test_create_using_my_own_data(self):
        mother = Mother(CSIExample, field_1='1,2,3', field_2='5,6')

        self.assertEqual('1,2,3', mother.field_1)
        self.assertEqual('5,6', mother.field_2)
