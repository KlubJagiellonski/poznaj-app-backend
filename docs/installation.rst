Installation instructions
=========================

Clone the repository
--------------------

Using the console, navigate to the root directory in which your projects live and clone this project's repository:
::

    $ git clone git@github.com:kj-wroclaw/poznajwroclaw-backend.git
    $ cd poznajwroclaw-backend

You may also wish to fork the repository on GitHub and clone the resultant personal fork.
This is advised if you are going to be doing development on poznajwroclaw-backend and contributing
to the project.

There are two ways to install poznajwroclaw-backend:

* :ref:`Stand-alone installation`
* :ref:`Docker-based installation`


It is recommended to use docker for local development.

.. _Stand-alone installation:

Stand-alone installation
------------------------

These instructions are specific to Ubuntu Linux but will be similar for other UNIX-based systems.

1. Install PostgreSQL:

::

    $ sudo apt-get update
    $ sudo apt-get install postgresql postgresql-contrib

2. Create database and user:

::

    $ su - postgres
    $ psql


3. Install `virtualenv`_  to be able to create a local environment for your server:

.. _virtualenv:

::

    $ pip install virtualenv

4. Create your virtual environment:

::

    $ virtualenv -p /usr/bin/python3 ~/.virtualenvs/poznajwroclaw-backend

Make sure that you have python 3 installed as we are using this version.

5. Activate your environment:

::

    $ source ~/.virtualenvs/poznajwroclaw-backend/bin/activate


6. Install local and test requirements:

::

    (poznajwroclaw-backend) $ pip install -r requirements/local.txt
    (poznajwroclaw-backend) $ pip install -r requirements/test.txt

7. Install `autoenv`_ and put there:

.. _autoenv:

::

    $ cat .env
    DATABASE_URL=postgres://poznajwroclaw:poznajwroclaw@localhost:5432/poznajwroclawdb

8. Then run server via:

::

    (poznajwroclaw-backend) $ python manage.py migrate
    (poznajwroclaw-backend) $ python manage.py runserver

9. To run tests use

::

    (poznajwroclaw-backend) $ pip install tox
    (poznajwroclaw-backend) $ tox

.. _Docker-based installation:

Docker-based installation
-------------------------

We are using docker and docker compose to develop code locally. Before
you run any commands below please make sure that you have docker installed
via this `instructions`_. As you have installed docker install docker-compose

.. _instructions: https://docker.github.io/engine/installation
::

    (poznajwroclaw-backend)$ pip install docker-compose

After this setup you are ready to go! First run application:
::

    $ make build
    $ make run

Then make migrations:
::

    $ make make-migrations

And migrate:
::

    $ make migrate

To create superuser use:
::

    $ docker-compose run django python manage.py createsuperuser

To run test (after you run ``make run``) use:
::

    $ make test

