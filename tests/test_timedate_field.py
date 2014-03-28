try:
    import unittest2 as unittest
except ImportError:
    import unittest

import datetime
from django.db import models

from django_mothers import Mother


class DateTimeExample(models.Model):
    field_1 = models.DateTimeField()
    field_2 = models.DateTimeField()


class TestDateFields(unittest.TestCase):
    def test_create_date_mother(self):
        mother = Mother(DateTimeExample)

        self.assertIsInstance(mother.field_1, datetime.datetime)
        self.assertIsInstance(mother.field_2, datetime.datetime)
