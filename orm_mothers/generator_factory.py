from django.db.models import fields
from . import generators


MAPPING = [
    (fields.CommaSeparatedIntegerField, generators.comma_separated_int),
    (fields.CharField, generators.string),
    (fields.NullBooleanField, generators.boolean_or_none),
    (fields.BooleanField, generators.boolean),
    (fields.PositiveSmallIntegerField, generators.positive_small_integer),
    (fields.SmallIntegerField, generators.small_integer),
    (fields.PositiveIntegerField, generators.positive_integer),
    (fields.IntegerField, generators.integer),
    (fields.DateTimeField, generators.datetime),
    (fields.DateField, generators.date),
    (fields.TimeField, generators.time),
]


def generate(field):
    for clazz, generator in MAPPING:
        if isinstance(field, clazz):
            return generator(field)
