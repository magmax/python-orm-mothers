import sys
if sys.version_info < (3, 0):
    import unittest2 as unittest
else:
    import unittest

from django.db import models

from orm_mothers import DjangoMother as Mother


class PositiveIntegerExample(models.Model):
    field_1 = models.PositiveIntegerField()
    field_2 = models.PositiveIntegerField()


class TestSmallIntegerFields(unittest.TestCase):
    def test_create_small_integer_mother(self):
        mother = Mother(PositiveIntegerExample)

        self.assertIsInstance(mother.field_1, int)
        self.assertIsInstance(mother.field_2, int)
        self.assertGreaterEqual(mother.field_1, 0)
        self.assertLessEqual(mother.field_1, 2147483647)
