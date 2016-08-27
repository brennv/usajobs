import usajobs
import pytest
import requests


def test_search():
    test_url = 'https://api.usa.gov/jobs/search.json?query=park+ranger&size=100'
    test_data = requests.get(test_url).json()
    results = usajobs.search('park ranger', step=5, as_dict=True)
    assert len(results) == len(test_data)  # hack
