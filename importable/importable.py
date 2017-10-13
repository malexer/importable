from abc import ABCMeta, abstractmethod
import atexit
import os.path
import shutil
import sys
import tempfile
from urllib.parse import urlparse
import zipfile

import requests


class ImportBase(metaclass=ABCMeta):

    def __init__(self):
        self._tmp_dir = None
        self._python_path = None
        self._local_package_file = None

    def _get_temp_filename(self):
        f = tempfile.NamedTemporaryFile(dir=self._tmp_dir, delete=False)
        f.close()
        os.unlink(f.name)
        return f.name

    def _create_temp_locations(self, temp_dir=None):
        if temp_dir is not None and not os.path.exists(temp_dir):
            raise IOError('Provided temp path does not exist: %s' % temp_dir)

        self._tmp_dir = tempfile.mkdtemp(dir=temp_dir)
        self._python_path = tempfile.mkdtemp(dir=self._tmp_dir)

        self._local_package_file = self._get_temp_filename()

        atexit.register(shutil.rmtree, path=self._tmp_dir, ignore_errors=True)

    def _add_to_python_path(self):
        if self._python_path is not None and os.path.exists(self._python_path):
            sys.path.insert(0, self._python_path)

    @abstractmethod
    def download(self, remote_location, local_filepath):
        pass

    @abstractmethod
    def unpack(self, source_file, destination_dir):
        pass

    def add_pkg_to_python_path(self, location):
        self._create_temp_locations()

        self.download(
            remote_location=location,
            local_filepath=self._local_package_file,
        )
        self.unpack(
            source_file=self._local_package_file,
            destination_dir=self._python_path,
        )

        self._add_to_python_path()


class HttpImporter(ImportBase):

    def download(self, remote_location, local_filepath):
        r = requests.get(remote_location, stream=True)


        if r.status_code != 200:
            r.raise_for_status()

        with open(local_filepath, 'wb') as f:
            for chunk in r.iter_content(1024*10):
                f.write(chunk)


class ZipImporter(ImportBase):

    def unpack(self, source_file, destination_dir):
        if not zipfile.is_zipfile(source_file):
            raise ValueError('Provided file is not a ZIP archive: %s' % source_file)

        with zipfile.ZipFile(source_file) as zf:
            zf.extractall(path=destination_dir)


class HttpZipImporter(HttpImporter, ZipImporter):
    pass


def get_url_schema(url):
    p = urlparse(url)
    if all([p.scheme, p.netloc, p.path]):
        return p.scheme


def importable(url):
    scheme = get_url_schema(url)
    if scheme:
        if scheme.startswith('http'):
            return HttpZipImporter().add_pkg_to_python_path(url)

    raise ValueError('Unsupported url format: %s' % url)
