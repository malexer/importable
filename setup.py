from setuptools import setup
from codecs import open
from os import path


cwd = path.abspath(path.dirname(__file__))


with open(path.join(cwd, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='importable',
    version='0.1.0',

    description='Allows to import zip-compressed Python package by URL.',
    long_description=long_description,
    url='https://github.com/malexer/importable',

    author='Alex (Oleksii) Markov',
    author_email='alex@markovs.me',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords=('import url importable python_path'),

    py_modules=['importable'],
    install_requires=[
        'requests',
    ],
)
