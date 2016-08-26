import usajobs
import pytest


def test_query_connect():
    results = usajobs.query('JobCategoryCode=2210')
    assert results != None


def test_search_connect():
    results = usajobs.search('park ranger')
    assert results != None
