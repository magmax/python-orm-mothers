Create fake objects automatically from any ORM models. Useful for testing.

ORM          | Current status
-------------|-------------------
[Django]     | Under development
[SQLAlchemy] | Not started

TESTS                                     | COVERAGE
------------------------------------------|----------
[![Travis status][travis image]][Travis]  |


# Description

Python-orm-mothers helps you to test your ORM-based applications. It is a replacement for _fixtures_.

The main idea is to be able to create in-memory objects, instead of static JSON files. This way you can decide to persist them or to use them without using a database.

Django-mothers allows you to create a new object based on the model. This framework will randomize all the fields (and maybe will create other related objects) in order to create a complete story about your object. It allows you to set some data to your desires too.

In the future, it should support [Django], [SQLAlchemy] or any other Python [ORM].

## Why "Mothers"?

Well... This work is based on a [Martin Fowler] post, [ObjectMother], where he described Object Mothers as:

> An object mother is a kind of class used in testing to help create example objects that you use for testing.

This post is based on a Paper written by Peter Schuh and Stephanie Punke, [Object Mother: Easing Test Object Creation in XP]. Here you have the Abstract:

> One of the most time-consuming and unfulfilling activities in testing is coding and maintaining test objects. The ObjectMother pattern addresses this issue by proposing a simple, scalable framework whose sole purpose is to construct and facilitate the customization of test objects. The pattern’s primary responsibilities are: to create test objects, to tailor those objects at any point during the testing process, and to terminate those objects once testing is complete. When the process of test-writing is made easier and the quality of test data more consistent, developers are likely to write more and better tests.

As you can assume, it is imposible to create any object with a logical history based in the ORM model. I mean: you cannot know that the field "name" refers to a person or a country. So this framework just generate random valid values for each case, allowing you to set any specific data.


# Show me the code

## Django examples

Here you have some simple and working examples.

Let's work with the model:

```python
from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=40)
    age  = models.IntegerField()
```

You can create a random `Person`:

```python
random_person = Mother(Person)
```

Or you can create a random `Person` with an specific age:

```python
person = Mother(Person, age=18)
```

The rest of fields will be randomized.

It's simple.

### Advanced usage

You can use a callable method as value if you want. It will receive the field as argument.

```python
import random
def random_age(field):
    return random.randint(14,80)

person = Mother(Person, age=random_age)
```

This allow you to assign the values you may need, instead of using the default ones.

# License

[![LGPL 3][LGPL image]][LGPL3]


# Current support

## Django ORM

Here you have a table with current support:

| Field name                         | support |
|------------------------------------|---------|
| AutoField                          | no      |
| BigIntegerField                    | **YES** |
| BinaryField                        | no      |
| BooleanField                       | **YES** |
| CharField                          | **YES** |
| CommaSeparatedIntegerField         | **YES** |
| DateField                          | **YES** |
| DateTimeField                      | **YES** |
| DecimalField                       | no      |
| EmailField                         | no      |
| FileField                          | no      |
| FilePathField                      | no      |
| FloatField                         | no      |
| ImageField                         | no      |
| IntegerField                       | **YES** |
| IPAddressField                     | no      |
| GenericIPAddressField              | no      |
| NullBooleanField                   | no      |
| PositiveIntegerField               | no      |
| PositiveSmallIntegerField          | no      |
| SlugField                          | no      |
| SmallIntegerField                  | no      |
| TextField                          | no      |
| TimeField                          | no      |
| URLField                           | no      |
| -- | |
| Foreign Key                        | no      |
| Many to Many                       | no      |
| One to One                         | no      |
| -- | |
| Cyclic relationships               | no      |


## SQLAlchemy ORM

Not started yet



[Django]: https://docs.djangoproject.com
[SQLAlchemy]: http://www.sqlalchemy.org/
[ORM]: http://en.wikipedia.org/wiki/Object-relational_mapping "Object-Relational Mapping"
[Travis]: https://travis-ci.org/magmax/python-orm-mothers
[travis image]:https://travis-ci.org/magmax/django-mothers.svg
[LGPL image]: https://www.gnu.org/graphics/lgplv3-147x51.png
[LGPL3]: https://www.gnu.org/licenses/gpl-3.0.html
[ObjectMother]: http://martinfowler.com/bliki/ObjectMother.html
[Object Mother: Easing Test Object Creation in XP]: http://cf.agilealliance.org/articles/system/article/file/910/file.pdf
[Martin Fowler]: http://martinfowler.com/
