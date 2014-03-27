import random
import string

from generators import (
    comma_separated_int
    )

from django.conf import settings
if not settings.configured:
    settings.configure(DEBUG=True)
from django.db.models import fields


class Mother(object):
    def __init__(self, model, **kwargs):
        self.model = model

        self.obj = model()

        for field in model._meta.fields:
            print field

            if field.name in kwargs:
                value = kwargs[field.name]
                if callable(value):
                    value = value(field.name)
                setattr(self.obj, field.name, value)
                continue

            if isinstance(field, fields.CommaSeparatedIntegerField):
                v = generators.comma_separated_int(field)
                setattr(self.obj, field.name, v)
                continue

            if isinstance(field, fields.CharField):
                v = generators.string(field)
                setattr(self.obj, field.name, v)
                continue

            if isinstance(field, fields.BooleanField):
                v = generators.boolean(field)
                setattr(self.obj, field.name, v)
                continue

            if isinstance(field, fields.IntegerField):
                v = generators.integer(field)
                setattr(self.obj, field.name, v)
                continue

    def __getattr__(self, attr):
        return getattr(self.obj, attr)
