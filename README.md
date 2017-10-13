# importable

Allows to import zip-compressed Python package by URL.

Download remote zip-compressed Python package, unzip and add to Python
path.

All temp files will be removed on exit unless Python process was
terminated.

Note: `import` should be called separatelly after calling `importable`. All
we do here - just adding package to local python path.


# Install

Using pip:

    $ pip install importable


# Usage

Make remote package importable, then import it and use:

```python
from importable import importable


# add contents of "<filename>.zip" to python path
importable('http://<url>/<filename>.zip')

# now you can import your module
import <module_name>
```


# Example

Assuming that you have local nginx serving `/var/www/html/` on port 80.

```bash
$ mkdir mymodule
$ echo "my_var = 'I want to import this one!'" > mymodule/__init__.py
$ zip -r mymodule.zip mymodule
$ rm ./mymodule
$ mv mymodule.zip /var/www/html
```
Then execute the python code:
```python
>>> from importable import importable
>>> importable('http://localhost/mymodule.zip')
>>> import mymodule
>>> print(mymodule.my_var)
I want to import this one!
```
