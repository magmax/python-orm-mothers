from django.db.models import fields
import generators


MAPPING = [
    (fields.CommaSeparatedIntegerField, generators.comma_separated_int),
    (fields.CharField, generators.string),
    (fields.BooleanField, generators.boolean),
    (fields.IntegerField, generators.integer),
    (fields.DateTimeField, generators.datetime),
    (fields.DateField, generators.date),
    (fields.TimeField, generators.time),
]

def generate(field):
    for clazz, generator in MAPPING:
        if isinstance(field, clazz):
            print(clazz)  ## FIXME
            return generator(field)
