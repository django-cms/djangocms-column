#!/usr/bin/env python
from pathlib import Path

from setuptools import setup

from djangocms_column import __version__

INSTALL_REQUIRES = [
    'django-cms>=3.8.0',
    'Django>=2.2'  # the maximum version should be dictated by the cms
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 2.2',
    'Framework :: Django :: 3.2',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
]

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    name='djangocms-column',
    version=__version__,
    description='Column Plugin for django CMS',
    author='Django CMS Association and contributors',
    author_email='info@django-cms.org',
    url='https://github.com/django-cms/djangocms-column',
    packages=[
        'djangocms_column',
        'djangocms_column.migrations',
    ],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    python_requires='>=3.7',
    zip_safe=False
)
