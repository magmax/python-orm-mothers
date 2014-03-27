import unittest


import unittest

from django.conf import settings
if not settings.configured:
    settings.configure(DEBUG=True)
from django.db import models

from django_mothers import Mother


class StringExample(models.Model):
    field_1 = models.CharField(max_length=10)
    field_2 = models.CharField()


class TestCharFields(unittest.TestCase):
    def test_create_string_mother(self):
        mother = Mother(StringExample)

        self.assertIsInstance(mother.field_1, str)
        self.assertIsInstance(mother.field_2, str)
