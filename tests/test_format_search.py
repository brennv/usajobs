import usajobs
import pytest


def test_format_search():
    url = usajobs.format_search('park ranger')
    assert url == 'https://api.usa.gov/jobs/search.json?query=park+ranger'
