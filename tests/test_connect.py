import usajobs
import pytest


def test_connect():
    email, apikey = 'email', 'apikey'
    headers = usajobs.connect(email=email, apikey=apikey)
    assert headers == {'Host': 'data.usajobs.gov',
                       'User-Agent': 'email',
                       'Authorization-Key': 'apikey'}
