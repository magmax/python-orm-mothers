import random
import string

import generator_factory

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

            v = generator_factory.generate(field)
            setattr(self.obj, field.name, v)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)
