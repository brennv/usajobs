import requests
from .connect import connect


def query(terms, auth=None):
    base_url = 'https://data.usajobs.gov/api/search?'
    url = base_url + terms  # like: JobCategoryCode=2210
    if not auth:
        env = namedtupled.env(['email', 'apikey'])
        auth = connect(email=env.email, apikey=env.apikey)
    resp = requests.get(url, headers=auth)
    data = resp.json()
    return data
