# coding: utf-8

from codecs import open
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

__version__ = None
with open(os.path.join(here, 'legipy', 'version.py')) as version:
    exec(version.read())
assert __version__ is not None

with open(os.path.join(here, 'README.md')) as readme:
    LONG_DESC = readme.read().decode('utf-8')

setup(
    name='legipy',
    version=__version__,

    description='Python client for legifrance.gouv.fr website',
    long_description=LONG_DESC,
    license="MIT",

    url='https://github.com/njoyard/legipy',
    author='Nicolas Joyard',
    author_email='joyard.nicolas@gmail.com',

    include_package_data=True,

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],

    keywords='scraping politics data france',

    packages=[
        'legipy'
    ],

    install_requires=[
        'beautifulsoup4',
        'html5lib',
        'requests'
    ],

    scripts=[],
)
