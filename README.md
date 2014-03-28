Create fake objects automatically from Django models. Useful for testing.

| **Current status** | In development.                           |
| :------------------------------------------------------------- |
| **Tests status**   | [![Travis status][travis status]][travis] |
| :------------------------------------------------------------- |


# Description

Django-mothers helps you to test your [Django] applications. It is a replacement for _fixtures_

The main idea is to be able to create in-memory objects, instead of static JSON files. This way you can decide to persist them or to use them without using a database.

Django-mothers allows you to create a new object based on the model. This framework will randomize all the fields (and maybe will create other related objects) in order to create a complete story about your object. It allows you to set some data to your desires too.


# Show me the code

Here you have some simple and working examples.

Let's work with the model:

    from django.db import models
    class Person(models.Model):
        name = models.CharField(max_length=40)
        age  = models.IntegerField()

You can create a random `Person`:

    random_person = Mother(Person)

Or you can create a random `Person` with an specific age:

    person = Mother(Person, age=18)

The rest of fields will be randomized.

It's simple.

## Advanced usage

You can use a callable method as value if you want. It will receive the field as argument.

    import random
    def random_age(field):
        return random.randint(14,80)

    person = Mother(Person, age=random_age)

This allow you to assign the values you may need, instead of using the default ones.

# License

LGPL3


# Current support

Here you have a table with current support:

| AutoField                          | no   |
| BigIntegerField                    | YES  |
| BinaryField                        | no   |
| BooleanField                       | YES  |
| CharField                          | YES  |
| CommaSeparatedIntegerField         | YES  |
| DateField                          | YES  |
| DateTimeField                      | YES  |
| DecimalField                       | no   |
| EmailField                         | no   |
| FileField                          | no   |
| FilePathField                      | no   |
| FloatField                         | no   |
| ImageField                         | no   |
| IntegerField                       | YES  |
| IPAddressField                     | no   |
| GenericIPAddressField              | no   |
| NullBooleanField                   | no   |
| PositiveIntegerField               | no   |
| PositiveSmallIntegerField          | no   |
| SlugField                          | no   |
| SmallIntegerField                  | no   |
| TextField                          | no   |
| TimeField                          | no   |
| URLField                           | no   |
| :---------------------------------------- |
| Foreign Key                        | no   |
| Many to Many                       | no   |
| One to One                         | no   |
| :---------------------------------------- |
| Cyclic relationships               | no   |



[Django]: https://docs.djangoproject.com
[Travis]: https://travis-ci.org/magmax/django-mothers
[travis status]:https://travis-ci.org/magmax/django-mothers.svg
