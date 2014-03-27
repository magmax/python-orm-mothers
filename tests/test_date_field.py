import unittest
import datetime
from django.db import models

from django_mothers import Mother


class DateExample(models.Model):
    field_1 = models.DateField()
    field_2 = models.DateField()


class TestDateFields(unittest.TestCase):
    def test_create_date_mother(self):
        mother = Mother(DateExample)

        self.assertIsInstance(mother.field_1, datetime.date)
        self.assertIsInstance(mother.field_2, datetime.date)
