from setuptools import setup


badged_description = """
.. image:: https://travis-ci.org/brennv/usajobs.svg?branch=master
    :target: https://travis-ci.org/brennv/usajobs
.. image:: https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5-blue.svg
.. image:: https://img.shields.io/codecov/c/github/brennv/usajobs.svg
    :target: https://codecov.io/gh/brennv/usajobs

`https://github.com/brennv/usajobs`_

.. _https://github.com/brennv/usajobs: https://github.com/brennv/usajobs
"""

setup(
    name='usajobs',
    packages=['usajobs'],
    version='0.1.4',
    description='Lightweight wrapper for the usajobs.gov api.',
    long_description=badged_description,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    author='brennv',
    author_email='brennan@beta.build',
    license='MIT',
    url='https://github.com/brennv/usajobs',
    download_url='https://github.com/brennv/usajobs/tarball/0.1.4',
    keywords='usajobs usajobs.gov api',
    install_requires=[
        'requests',
        'nametupled',
    ],
    include_package_data=True,
    zip_safe=False)
