import random
import string as string_mod
import datetime as datetime_mod


def comma_separated_int(field):
    v = [str(integer(field))
         for _ in range(random.randrange(0, 5))]
    return ','.join(v)


def string(field):
    length = field.max_length or 10
    return _random_string(length)


def _random_string(size):
    chars = string_mod.ascii_uppercase + string_mod.digits
    return ''.join(random.choice(chars) for _ in range(size))


def boolean(field):
    return random.choice((True, False))


def integer(field):
    return random.randint(-2147483648, 2147483647)


def datetime(field):
    return datetime_mod.datetime.fromtimestamp(integer(field))


def date(field):
    return datetime(field).date()


def time(field):
    return datetime(field).time()
