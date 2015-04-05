# -*- coding: utf-8 -*-
import io
import os
import re
from setuptools import setup


PACKAGE = 'pyceo'
NAME = 'pyCEO'
URL = 'http://github.com/lucuma/pyCEO'
DESCRIPTION = 'Create management scripts for your applications'

AUTHOR = 'Juan-Pablo Scaletti'
AUTHOR_EMAIL = 'juanpablo@lucumalabs.com'

THIS_DIR = os.path.dirname(__file__).rstrip('/')


def get_path(*args):
    return os.path.join(THIS_DIR, *args)


def read_from(filepath):
    with io.open(filepath, 'rt', encoding='utf-8') as f:
        source = f.read()
    return source


def get_version():
    data = read_from(get_path(PACKAGE, '__init__.py'))
    version = re.search(r"__version__\s*=\s*'([^']+)'", data).group(1)
    return version


def find_package_data(root, include_files=None):
    include_files = include_files or ['.gitignore', ]
    files = []
    src_root = get_path(root).rstrip('/') + '/'
    for dirpath, subdirs, filenames in os.walk(src_root):
        path, dirname = os.path.split(dirpath)
        if dirname.startswith(('.', '_')):
            continue
        dirpath = dirpath.replace(src_root, '')
        for filename in filenames:
            is_valid_filename = not (
                filename.startswith('.') or
                filename.endswith('.pyc')
            )
            include_it_anyway = filename in include_files

            if is_valid_filename or include_it_anyway:
                files.append(os.path.join(dirpath, filename))
    return files


def find_packages_data(*roots):
    return dict([(root, find_package_data(root)) for root in roots])


def get_requirements():
    data = read_from(get_path('requirements.txt'))
    lines = map(lambda s: s.strip(), data.splitlines())
    return [l for l in lines if l and not l.startswith('#')]


def run_tests():
    import sys
    import subprocess
    errno = subprocess.call([sys.executable, 'runtests.py'])
    raise SystemExit(errno)


setup(
    name=NAME,
    version=get_version(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=[PACKAGE],
    package_data=find_packages_data(PACKAGE, 'tests'),
    zip_safe=False,
    url=URL,
    license='MIT license (see LICENSE)',
    description=DESCRIPTION,
    long_description=read_from(get_path('README.rst')),
    install_requires=get_requirements(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='__main__.run_tests'
)
