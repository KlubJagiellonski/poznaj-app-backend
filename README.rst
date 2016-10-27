Poznaj Wrocław
==============

.. image:: https://travis-ci.org/kj-wroclaw/poznajwroclaw-backend.svg?branch=master
    :target: https://travis-ci.org/kj-wroclaw/poznajwroclaw-backend
    :alt: Build Status

.. image:: https://readthedocs.org/projects/poznajwroclaw-backend/badge/?version=latest
    :target: http://poznajwroclaw-backend.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


This `Django`_ project includes code for backend of Poznaj Wrocław application. It tries to follow
`12 Factor App Guinness <https://12factor.net/>`_.

.. _Django: <https://www.djangoproject.com/>

Quickstart
----------

Full `installation`_ instructions.

.. _installation: http://poznajwroclaw-backend.readthedocs.io/en/latest/installation.html


To develop locally we use docker + docker compose. First make sure that you
installed docker by following these instructions: `link <https://docker.github.io/engine/installation/>`_.
Then run this command to run server & apply migrations.::

    $ make build
    $ make run
    $ make migrate


Documentation
-------------

Documentation for this project is available in the `docs`_ directory and `online`_.

.. _docs: https://github.com/kj-wroclaw/poznajwroclaw-backend/tree/master/docs

.. _online: http://poznajwroclaw-backend.readthedocs.io/en/latest/index.html


If you would like to browse the documentation locally, you can do so with `sphinx`:
::

    $ git clone git@github.com:kj-wroclaw/poznajwroclaw-backend.git
    $ cd poznajwroclaw-backend
    $ pip install virtualenv
    $ virtualenv -p /usr/bin/python3 ~/.virtualenvs/poznajwroclaw-backend
    $ source ~/.virtualenvs/poznajwroclaw-backend/bin/activate
    (poznajwroclaw-backend) $ pip install -r requirements/local.txt
    (poznajwroclaw-backend) $ cd docs
    (poznajwroclaw-backend) $ make html
    (poznajwroclaw-backend) $ sphinx-autobuild . _build_html


Getting help
------------

Use the `issue tracker <https://github.com/kj-wroclaw/poznajwroclaw-backend/issues>`_ to follow the development conversation.
If you find a bug not listed in the issue tracker, please `file a bug report <https://github.com/kj-wroclaw/poznajwroclaw-backend/issues/new>`_.

Getting involved
----------------

We welcome your feedback and contributions. See the `contribution guidelines`_ for more details.

.. _contribution guidelines <https://github.com/kj-wroclaw/poznajwroclaw-backend/blob/master/.github/CONTRIBUTING.md>:


License
-------

1. `LICENSE <https://github.com/kj-wroclaw/poznajwroclaw-backend/blob/master/LICENSE>`_


Credits
-------

1. `Cookiecutter-django`_
2. `Cfgov-refresh`_
3. `Open-source-project-template`_

.. _Cookiecutter-django: https://github.com/pydanny/cookiecutter-django
.. _Cfgov-refresh: https://github.com/cfpb/cfgov-refresh
.. _Open-source-project-template: https://github.com/cfpb/open-source-project-template
