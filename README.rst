Poznaj Wrocław
==============

This is repo containing code for backend of Poznaj Wrocław application.

Development
-----------

To develop locally we use docker + docker compose. First make sure that you
installed docker by following these instructions: `link <https://docker.github.io/engine/installation/>`_.
Then install `docker-compose <https://docs.docker.com/compose/>`_ by:
::

    $ pip install docker-compose

After this setup you are ready to go! First run application:
::

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
