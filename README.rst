.. image:: https://travis-ci.org/brennv/usajobs.svg?branch=master
    :target: https://travis-ci.org/brennv/usajobs
.. image:: https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5-blue.svg
.. image:: https://img.shields.io/codecov/c/github/brennv/usajobs.svg
    :target: https://codecov.io/gh/brennv/usajobs

usajobs
=======

Lightweight wrapper for exploring `api.usa.gov/jobs`_ and `data.usajobs.gov/api`_. Thanks to `DigitalGov`_ and `GSA`_.

Installation
------------

.. code:: bash

    pip install usajobs

Getting started
---------------

.. code:: python

    import usajobs

    results = usajobs.search('manager')

    len(results)              # 1392
    result = results[0]       # let's look at the first result

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

Usage
-----

The method `search`_ currently exposes `api.usa.gov/jobs`_ which allows for 'fuzzy' searching. 

search()
~~~~~~~~

Return results from search terms using the `api.usa.gov/jobs`_.

*arguments: terms, start=0, step=100, as_dict=False, sleep=0.1, data=[]*

Results, by default, are a list of nametupled data accessible as follows:

.. code:: python

    results = usajobs.search('park ranger')

    len(results)                # 22

    results[0].url              # 'https://www.usajobs.gov/GetJob/ViewDetails/426475700'

    results[0]._asdict().keys() # odict_keys(['id', 'organization_name', 'start_date', 'locations', 'position_title', 'url', 'minimum', 'end_date', 'maximum', 'rate_interval_code'])

To return the results as a list of dicts, use *as_dict* argument:

.. code:: python

    results = usajobs.search('park ranger', as_dict=True)

    print(results[0])

.. code:: javascript

    {
      'id': 'usajobs:426475700',
      'position_title': 'Park Ranger',
      'organization_name': 'Bureau of Land Management',
      'rate_interval_code': 'PH',
      'minimum': 15,
      'maximum': 20,
      'start_date': '2016-01-18',
      'end_date': '2016-08-31',
      'locations': ['Lake Havasu City, AZ', 'Butte, MT'],
      'url': 'https://www.usajobs.gov/GetJob/ViewDetails/426475700'
    }

Development
-----------

PRs welcome, tests run with:

.. code:: bash

    pip install pytest pytest-cov
    python -m pytest tests --cov=usajobs/

.. _search: #search
.. _data.usajobs.gov/api: https://developer.usajobs.gov/Search-API/Instantiating-the-API
.. _api.usa.gov/jobs: http://search.digitalgov.gov/developer/jobs.html
.. _GSA: https://github.com/GSA/jobs_api
.. _DigitalGov: http://search.digitalgov.gov/index.html
