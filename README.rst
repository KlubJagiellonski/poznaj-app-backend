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


Licence
-----------
Copyright 2016 Poznaj Wrocław

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
