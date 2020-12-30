pgbak
=====

PostgreSQL backup script - local or S3. Following LinuxAcademy Python 3 scripting guide

Prep
----

1. Verify ``pip`` and ``pipenv`` are installed.
2. Clone repo: ``git clone git@github.com:kurkoleg/pgbak``
3. From the repo: fetch dev dependencies ``make install``
4. Launch virtualenv: ``pipenv shell``

Usage
-----

Pass in 3 arguments - database url, storage driver (local or s3), and destination

S3 example using bucket path:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local example using local path:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/log/db_one/backups/dump.sql



Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active

::

    $ pipenv run make






