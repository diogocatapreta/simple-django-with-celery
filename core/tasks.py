from __future__ import absolute_import, unicode_literals
import random
from celerysample.celery import app as celery_app



@celery_app.task(name='core.tasks.add')
def add(x, y):
    return x + y


@celery_app.task(name="core.tasks.multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total


@celery_app.task(name="core.tasks.sum_list")
def listsum(numbers):
    return sum(numbers)
