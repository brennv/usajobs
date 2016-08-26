usajobs
=======

Lightweight wrapper for exploring the `v3 usajobs.gov api`_.

Installation
------------

.. code:: bash

    pip install usajobs

Getting started
---------------

.. code:: python

    import usajobs

    results = usajobs.search('park ranger')

    len(results)            # 25
    result = results[0]     # let's look at the first result

    result.id               # 'usajobs:426475700'
    result.position_title   # 'Park Ranger'
    result.start_date       # '2016-01-18'
    result.end_date         # '2016-08-31'
    result.url              # 'https://www.usajobs.gov/GetJob/ViewDetails/426475700'
    result.locations        # ['Lake Havasu City, AZ', 'Butte, MT']

Usage
-----

The method `search`_ exposes the v3 api which allows for 'fuzzy' searching.

search()
~~~~~~~~

Return results of fuzzy searches from search terms using the `v3 usajobs.gov api`_.

*arguments: terms, as_dict=False*

Results, by default, are a list of nametupled data accessible as follows:

.. code:: python

    results = usajobs.search('park ranger')

    results[0].id               # 'usajobs:426475700'
    results[0].position_title   # 'Park Ranger'
    results[0].start_date       # '2016-01-18'
    results[0].end_date         # '2016-08-31'
    results[0].url              # 'https://www.usajobs.gov/GetJob/ViewDetails/426475700'
    results[0].locations        # ['Lake Havasu City, AZ', 'Butte, MT']

To return the results as a list of dicts, use the `as_dict` argument:

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
.. _v2 usajobs.gov api: https://developer.usajobs.gov/Search-API/Instantiating-the-API
.. _v3 usajobs.gov api: http://search.digitalgov.gov/developer/jobs.html
