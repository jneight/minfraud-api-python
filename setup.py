#!/usr/bin/env python

import ast
import io
import re

# This is necessary for Python 2.6 on Travis for some reason.
import multiprocessing

from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with io.open('minfraud/version.py', 'r', encoding='utf-8') as f:
    _version = str(ast.literal_eval(_version_re.search(f.read()).group(1)))

with io.open('README.rst', 'r', encoding='utf-8') as f:
    _readme = f.read()

setup(
    name='minfraud',
    version=_version,
    description='MaxMind minFraud Score, Insights, and Factors API',
    long_description=_readme,
    author='Gregory Oschwald',
    author_email='goschwald@maxmind.com',
    url='http://www.maxmind.com/',
    packages=['minfraud'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'geoip2>=2.6.0',
        'requests>=2.7',
        'rfc3987',
        'strict-rfc3339',
        'validate_email',
        'voluptuous',
    ],
    extras_require={
        ':python_version=="2.6" or python_version=="2.7"': ['ipaddress']
    },
    tests_require=['requests_mock'],
    test_suite="tests",
    license='Apache License 2.0 ',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet',
    ], )
