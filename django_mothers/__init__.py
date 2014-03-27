import random
import string

from django.conf import settings
if not settings.configured:
    settings.configure(DEBUG=True)
from django.db.models import fields


def randomstring(size):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


class Mother(object):
    def __init__(self, model, **kwargs):
        self.model = model

        self.obj = model()

        for field in model._meta.fields:
            print field

            if field.name in kwargs:
                setattr(self.obj, field.name, kwargs[field.name])
                continue

            if isinstance(field, fields.CharField):
                length = field.max_length or 10
                setattr(self.obj, field.name, randomstring(length))
                continue

            if isinstance(field, fields.IntegerField):
                setattr(self.obj, field.name, random.randint(-2147483648, 2147483647))
                continue

    def __getattr__(self, attr):
        return getattr(self.obj, attr)
