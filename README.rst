deploy_cookie_0
===============

I don't know man

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy deploy_cookie_0

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html

If you run into Mailgun configuration issues please for the sake of your time look into these resources:

Help with the subdomain DNS setup: https://simpleisbetterthancomplex.com/tutorial/2017/05/27/how-to-configure-mailgun-to-send-emails-in-a-django-app.html
Actual issue being opened on Cookiecutter-Django = https://github.com/pydanny/cookiecutter-django/issues/1705
More Isuues on Mailgun-1: https://github.com/pydanny/cookiecutter-django/issues/788
More Isuues on Mailgun-2: https://github.com/pydanny/cookiecutter-django/pull/1545
More Isuues on Mailgun-3: https://github.com/pydanny/cookiecutter-django/pull/1545/files/82dcd2d30c3ad358407ac5a4aa7c864ed5aec49a
Django-anymail: https://github.com/anymail/django-anymail
finally the  MAILGUN: mailgun.com
