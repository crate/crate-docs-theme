=====================
Code snippet examples
=====================


SQL
===

.. highlight:: psql

Plain
-----

::

    ALTER TABLE foo ADD COLUMN new_column INTEGER;

With prompts
------------

::

    mysql> CREATE TABLE foo (
    ...       id integer primary key,
    ...       name varchar(255),
    ...       date datetime,
    ...       fruits set('apple', 'pear', 'banana')
    ...    ) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

::

    cr> COPY foo_imported FROM '/tmp/dump.csv' WITH (bulk_size=1000);

With prompts and doctests
-------------------------

::

    cr> CREATE TABLE metrics1 (
    ...     weight REAL CONSTRAINT weight_is_positive CHECK (weight >= 0),
    ... );
    CREATE OK, 1 row affected  (... sec)

::

    cr> drop table metrics1;
    DROP OK, 1 row affected (... sec)

::

    cr> select array(select height from sys.summits order by height desc limit 5)
    ... as top5_mountains_array;
    +--------------------------------+
    | top5_mountains_array           |
    +--------------------------------+
    | [4808, 4634, 4545, 4527, 4506] |
    +--------------------------------+
    SELECT 1 row in set (... sec)


Configuration files
===================

.. code-block:: ini

    [client]
    default-character-set=utf8
    [mysqld]
    character-set-server=utf8


Terminal commands
=================

.. code-block:: sh

    sh$ csvsql --db crate://localhost:4200 --insert /tmp/dump.csv


Code blocks
===========

With prompts and empty lines
----------------------------

This snippet can be used to verify that ``sphinx-copybutton`` works
appropriately by also honoring empty lines.

.. code-block:: python

    >>> from sqlalchemy.ext import declarative
    >>> from crate.client.sqlalchemy import types
    >>> from uuid import uuid4

    >>> def gen_key():
    ...     return str(uuid4())
