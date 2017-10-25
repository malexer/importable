from setuptools import setup
from codecs import open
from os import path


cwd = path.abspath(path.dirname(__file__))


with open(path.join(cwd, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(cwd, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().split()

setup(
    name='importable',
    version='0.2.0',

    description=(
        'Allows to import zip-compressed Python package by URL (http, hdfs).'),
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

    keywords=('import url http hdfs zip importable python_path'),

    py_modules=['importable'],
    install_requires=requirements,
)
