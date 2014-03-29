import sys
if sys.version_info < (3, 0):
    import unittest2 as unittest
else:
    import unittest

from django.db import models

from orm_mothers import DjangoMother as Mother


class NullBooleanExample(models.Model):
    field_1 = models.NullBooleanField()
    field_2 = models.NullBooleanField()


class TestNullBooleanFields(unittest.TestCase):
    def test_create_nullboolean_mother(self):
        mother = Mother(NullBooleanExample)

        self.assertTrue(
            mother.field_1 is None
            or isinstance(mother.field_1, bool),
            "Expected boolean or None, but %s found" % mother.field_1
        )
        self.assertTrue(
            mother.field_2 is None
            or isinstance(mother.field_1, bool),
            "Expected boolean or None, but %s found" % mother.field_2
        )

    def test_create_using_my_own_data(self):
        mother = Mother(NullBooleanExample, field_1=True, field_2=None)

        self.assertTrue(mother.field_1)
        self.assertIsNone(mother.field_2)

    def test_assert_it_is_eventually_none(self):
        with self.assertRaises(AssertionError):
            for retry in range(1000):
                mother = Mother(NullBooleanExample)
                self.assertIsNone(mother.field_1)
