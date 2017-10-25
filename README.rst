importable
==========

Allows to import zip-compressed Python package by URL.

Download remote zip-compressed Python package, unzip and add to Python
path.

All temp files will be removed on exit unless Python process was
terminated.

Note: ``import`` should be called separatelly after calling
``importable``. All we do here - just adding package to local python path.


Supported URL types
-------------------

importable supports a limited set of URL types:

1. Http url to zip file: ``http(s)://<url>/<filename>.zip``

   The module, which you are going to import, should be located on the
   first level of <filename>.zip

   See section Example.

2. Http url to zip file on GitHub:
   ``http(s)://github.com/<path>/<filename>.zip``

   Similar to the previous type except that module is located inside an
   additional directory (in <filename>.zip).

3. Hdfs url to zip file: ``webhdfs://<host>:<port>/<path>/<filename>.zip``

   Similar to #1 except that file will be downloaded from HDFS.

   ``<host>`` - hostname or IP address of Hdfs namenode
   ``<port>`` - WebHdfs port of namenode


Install
-------

Using pip::

    $ pip install importable


Usage
-----

Make remote package importable, then import it and use:

.. code-block:: python

    from importable import importable


    # add contents of "<filename>.zip" to python path
    importable('http://<url>/<filename>.zip')

    # now you can import your module
    import <module_name>


Example
-------

Assuming that you have local nginx serving ``/var/www/html/`` on port 80.

.. code-block:: shell

    $ mkdir mymodule
    $ echo "my_var = 'I want to import this one!'" > mymodule/__init__.py
    $ zip -r mymodule.zip mymodule
    $ mv mymodule.zip /var/www/html

Then execute the python code:

.. code-block:: python

    >>> import mymodule
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: No module named 'mymodule'
    >>> from importable import importable
    >>> importable('http://localhost/mymodule.zip')
    >>> import mymodule
    >>> print(mymodule.my_var)
    I want to import this one!
