"""Tests for url parsing and choosing correct *Importer for processing."""

from unittest.mock import patch

import pytest

from importable.importable import importable, HttpZipImporter, \
    GitHubHttpZipImporter, HdfsZipImporter


@patch.object(HdfsZipImporter, 'add_pkg_to_python_path')
@patch.object(GitHubHttpZipImporter, 'add_pkg_to_python_path')
@patch.object(HttpZipImporter, 'add_pkg_to_python_path')
class TestIsMineChecks(object):

    def test_github_http(self, http, github, hdfs):
        importable('http://github.com/malexer/meteocalc/archive/master.zip')
        assert github.called
        assert not http.called
        assert not hdfs.called

    def test_github_https(self, http, github, hdfs):
        importable('https://github.com/malexer/meteocalc/archive/master.zip')
        assert github.called
        assert not http.called
        assert not hdfs.called

    def test_regular_http(self, http, github, hdfs):
        importable('http://www.somerepository.com/path/to/mymodule.zip')
        assert not github.called
        assert http.called
        assert not hdfs.called

    def test_regular_https(self, http, github, hdfs):
        importable('https://www.somerepository.com/path/to/mymodule.zip')
        assert not github.called
        assert http.called
        assert not hdfs.called

    def test_regular_http_with_port(self, http, github, hdfs):
        importable('http://localhost:8080/mymodule.zip')
        assert not github.called
        assert http.called
        assert not hdfs.called

    def test_regular_https_with_port(self, http, github, hdfs):
        importable('http://localhost:8080/folder1/mymodule.zip')
        assert not github.called
        assert http.called
        assert not hdfs.called

    def test_webhdfs(self, http, github, hdfs):
        importable('webhdfs://localhost/dir/mymodule.zip')
        assert not github.called
        assert not http.called
        assert hdfs.called

    def test_webhdfs_with_port(self, http, github, hdfs):
        importable('webhdfs://localhost:8080/dir/mymodule.zip')
        assert not github.called
        assert not http.called
        assert hdfs.called

    def test_no_match_for_ftp(self, http, github, hdfs):
        with pytest.raises(ValueError):
            importable('ftp://localhost/dir/mymodule.zip')

    def test_no_match_for_hdfs(self, http, github, hdfs):
        with pytest.raises(ValueError):
            importable('hdfs://localhost/dir/mymodule.zip')

    def test_not_a_url(self, http, github, hdfs):
        with pytest.raises(ValueError):
            importable('Just some text.')

    def test_empty_str(self, http, github, hdfs):
        with pytest.raises(ValueError):
            importable('')

    def test_with_none(self, http, github, hdfs):
        with pytest.raises(TypeError):
            importable(None)

    def test_with_int(self, http, github, hdfs):
        with pytest.raises(TypeError):
            importable(123)
