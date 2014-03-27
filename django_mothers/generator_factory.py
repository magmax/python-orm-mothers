from django.db.models import fields
import generators


MAPPING = [
    (fields.CommaSeparatedIntegerField, generators.comma_separated_int),
    (fields.CharField, generators.string),
    (fields.BooleanField, generators.boolean),
    (fields.IntegerField, generators.integer),
]

def generate(field):
    for clazz, generator in MAPPING:
        if isinstance(field, clazz):
            return generator(field)
