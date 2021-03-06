import sys
if sys.version_info < (3, 0):
    import unittest2 as unittest
else:
    import unittest

import datetime
from django.db import models

from orm_mothers import DjangoMother as Mother


class DateExample(models.Model):
    field_1 = models.DateField()
    field_2 = models.DateField()


class TestDateFields(unittest.TestCase):
    def test_create_date_mother(self):
        mother = Mother(DateExample)

        self.assertIsInstance(mother.field_1, datetime.date)
        self.assertIsInstance(mother.field_2, datetime.date)
