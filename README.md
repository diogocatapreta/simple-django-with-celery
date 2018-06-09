# Simple Django Project with Celery

This is a simple django project that use Celery to execute asynchronous jobs.
Celery is a powerful, production-ready asynchronous job queue, which allows you to run time-consuming Python functions in the background.

⚠ Warning this samples was using:
- Celery 4.1.1
- Django 2.0.6
- Python 3.6.6

## Prerequisites

### Install Python

Install [Python](https://www.python.org/downloads/) (if you're in linux, python 2.7 is already installed), [pip](https://pip.pypa.io/en/latest/installing.html), [django](https://docs.djangoproject.com/en/1.8/topics/install/) (and run `./manage.py syncdb`), [celery](http://www.celeryproject.org/install/), and django-celery


### Install Broker

Choose your celery broker and install that: [RabbitMQ](http://celery.readthedocs.org/en/latest/getting-started/brokers/rabbitmq.html), [Redis](http://celery.readthedocs.org/en/latest/getting-started/brokers/redis.html), [others...](http://celery.readthedocs.org/en/latest/getting-started/brokers/)

For this sample, I choose Redis.
The first piece of software we’ll install is Redis.
```
$ sudo aptitude install redis-server
```
## Setup Celery
Setup django-celery part 1: http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-the-django-orm-cache-as-a-result-backend

Setup django-celery part 2: https://github.com/celery/django-celery/blob/master/README.rst#using-django-celery


## Start All Things

### Start Django
Start Django: `./manage.py runserver` (and `./manage.py runserver $IP:$PORT` in Cloud 9)

### Start Redis
```
$ redis-server --version
```

### Execute Celery
How to execute Celery on terminal.
```
celery --app=celarysample.celery:app  -A celerysample worker -l info
```

### How to test on Shell
```
$ python manage.py shell

>>> from core.tasks import add
>>> add.delay(1,1)
```
