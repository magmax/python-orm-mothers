import sys
if sys.version_info < (3, 0):
    import unittest2 as unittest
else:
    import unittest

from django.db import models

from orm_mothers import DjangoMother as Mother


class AutoFieldExample(models.Model):
    field_1 = models.AutoField(primary_key=True)


class TestAutoFields(unittest.TestCase):
    def test_create_auto_mother(self):
        mother = Mother(AutoFieldExample)

        self.assertIsInstance(mother.field_1, int)

    def test_increasing(self):
        mother_1 = Mother(AutoFieldExample)
        mother_2 = Mother(AutoFieldExample)

        self.assertEqual(mother_1.field_1 + 1, mother_2.field_1)
