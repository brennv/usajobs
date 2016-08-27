from setuptools import setup


brief_description = """
.. image:: https://travis-ci.org/brennv/usajobs.svg?branch=master
    :target: https://travis-ci.org/brennv/usajobs
.. image:: https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5-blue.svg
.. image:: https://img.shields.io/codecov/c/github/brennv/usajobs.svg
    :target: https://codecov.io/gh/brennv/usajobs

`https://github.com/brennv/usajobs`_

Installation
============

.. code:: bash

    pip install usajobs

Getting started
===============

.. code:: python

    import usajobs

    results = usajobs.search('manager')

    len(results)              # 1392

    result = results[0]       # first result
    result.id                 # 'usajobs:445507500'
    result.organization_name  # 'National Park Service'
    result.position_title     # 'Project Manager (Interdisciplinary)'
    result.start_date         # '2016-08-23'
    result.end_date           # '2016-09-13'
    result.url                # 'https://www.usajobs.gov/GetJob/ViewDetails/445507500'
    result.locations          # ['Vancouver, WA']
    result.minimum            # 71012
    result.maximum            # 92316
    result.rate_interval_code # 'PA'

.. _https://github.com/brennv/usajobs: https://github.com/brennv/usajobs
"""

setup(
    name='usajobs',
    packages=['usajobs'],
    version='0.1.5',
    description='Wrapper for searching usajobs.gov.',
    long_description=brief_description,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    author='brennv',
    author_email='brennan@beta.build',
    license='MIT',
    url='https://github.com/brennv/usajobs',
    download_url='https://github.com/brennv/usajobs/tarball/0.1.5',
    keywords='usajobs usa.jobs usajobs.gov api',
    install_requires=[
        'requests',
        'nametupled',
    ],
    include_package_data=True,
    zip_safe=False)
