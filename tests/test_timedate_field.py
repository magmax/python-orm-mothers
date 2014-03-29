import sys
if sys.version_info < (3, 0):
    import unittest2 as unittest
else:
    import unittest

import datetime
from django.db import models

from orm_mothers import DjangoMother as Mother


class DateTimeExample(models.Model):
    field_1 = models.DateTimeField()
    field_2 = models.DateTimeField()


class TestDateFields(unittest.TestCase):
    def test_create_date_mother(self):
        mother = Mother(DateTimeExample)

        self.assertIsInstance(mother.field_1, datetime.datetime)
        self.assertIsInstance(mother.field_2, datetime.datetime)
