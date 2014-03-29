import sys
if sys.version < (3, 0):
    import unittest2 as unittest
else:
    import unittest

import datetime
from django.db import models

from django_mothers import Mother


class TimeExample(models.Model):
    field_1 = models.TimeField()
    field_2 = models.TimeField()


class TestDateFields(unittest.TestCase):
    def test_create_date_mother(self):
        mother = Mother(TimeExample)

        self.assertIsInstance(mother.field_1, datetime.time)
        self.assertIsInstance(mother.field_2, datetime.time)
