"""Tests for helper functions."""

from importable.importable import get_url_schema


def test_get_url_schema_http():
    assert 'http' == get_url_schema('http://localhost/mymodule.zip')
    assert 'http' == get_url_schema(
        'http://github.com/malexer/meteocalc/archive/master.zip')

    assert 'http' == get_url_schema('http://localhost:8080/mymodule.zip')
    assert 'http' == get_url_schema('http://localhost')


def test_get_url_schema_https():
    assert 'https' == get_url_schema('https://localhost/mymodule.zip')
    assert 'https' == get_url_schema(
        'https://github.com/malexer/meteocalc/archive/master.zip')

    assert 'https' == get_url_schema('https://localhost:8080/mymodule.zip')
    assert 'https' == get_url_schema('https://localhost')


def test_get_url_schema_webhdfs():
    assert 'webhdfs' == get_url_schema('webhdfs://localhost/mymodule.zip')
    assert 'webhdfs' == get_url_schema(
        'webhdfs://github.com/malexer/meteocalc/archive/master.zip')

    assert 'webhdfs' == get_url_schema('webhdfs://localhost:8080/mymodule.zip')
    assert 'webhdfs' == get_url_schema('webhdfs:///mymodule.zip')
