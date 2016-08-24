usajobs
=======

Lightweight wrapper for exploring the `usajobs.gov`_ api.

Installation
------------

.. code:: bash

    pip install usajobs

Getting started
---------------

.. code:: python

    import usajobs


    auth = usajobs.connect(email='your-email', apikey='your-api-key')

    results = usajobs.search('title=ranger', auth=auth)

    results  # {'SearchParameters': {}, 'SearchResult': ..

Usage
-----

Search usajobs with the following methods: `search`_, ..

To save yourself some typing for auth, in Terminal run:

.. code:: bash

    export email="your-email"
    export apikey="your-apikey"

search()
~~~~~~~~

At the moment search simply returns a dict with the entire response.

.. code:: python

    results = usajobs.search('title=ranger')

We'll Eeplore the data mostly using dict method `keys()`

.. code:: python

    results.keys()  # dict_keys(['SearchParameters', 'SearchResult', 'LanguageCode'])

    results['SearchResult'].keys()  # dict_keys(['SearchResultItems', 'UserArea', 'SearchResultCount', 'SearchResultCountAll'])

    results['SearchResult']['SearchResultItems'].keys()  # AttributeError: 'list' object has no attribute 'keys'

Got an error cause we hit a list, so we'll grab the first item in the list.

.. code:: python

    results['SearchResult']['SearchResultItems'][0]  # {'RelevanceRank': 10408.0, 'MatchedObjectDescriptor': ..

    results['SearchResult']['SearchResultItems'][0].keys()  # dict_keys(['RelevanceRank', 'MatchedObjectDescriptor', 'MatchedObjectId'])

    results['SearchResult']['SearchResultItems'][0]['MatchedObjectDescriptor'].keys()  # dict_keys(['PositionLocation', 'PositionID', 'PositionTitle', 'PositionRemuneration', 'JobCategory', 'PositionFormattedDescription', 'UserArea', 'PositionURI', 'PositionStartDate', 'OrganizationName', 'JobGrade', 'DepartmentName', 'QualificationSummary', 'PositionOfferingType', 'PublicationStartDate', 'ApplicationCloseDate', 'PositionEndDate', 'ApplyURI', 'PositionSchedule'])

PositionLocation looks interesting so we'll grab it.

.. code:: python

    data = results['SearchResult']['SearchResultItems'][0]['MatchedObjectDescriptor']['PositionLocation'][0]

    data  # [{'Longitude': -86.585, 'CityName': 'Huntsville, Alabama', 'Latitude': 34.7291, 'LocationName': 'Huntsville, Alabama', 'CountryCode': 'United States', 'CountrySubDivisionCode': 'Alabama'}]

    lon = data[0]['Longitude']
    lat = data[0]['Latitude']

    lon  # -86.585
    lat  # 34.7291

Next up, we'll add function to parse the locations for all the job results..


Development
-----------

PRs welcome, tests run with:

.. code:: bash

    pip install pytest pytest-cov
    python -m pytest tests --cov=usajobs/

.. _jobs: #jobs
.. _usajobs.gov: https://developer.usajobs.gov/Search-API/Instantiating-the-API
