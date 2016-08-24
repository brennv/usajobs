import usajobs
import pytest


def test_search():
    search = usajobs.search('JobCategoryCode=2210')
    assert search != None
