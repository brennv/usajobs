import requests
import namedtupled
# api v3: http://search.digitalgov.gov/developer/jobs.html


def format_search(terms):
    base_url = 'https://api.usa.gov/jobs/search.json?'
    words = [x for x in terms.split(' ') if x]
    query = 'query=' + '+'.join(words)
    url = base_url + query
    return url


def search(terms, start=0, step=100, as_dict=False):
    """ Constructs v3 fuzzy searches with parameters outlined here:
    http://search.digitalgov.gov/developer/jobs.html """
    size = '&size=' + str(step)
    base_url = format_search(terms) + size
    results = requests.get(base_url).json()
    data = results
    if len(data) == step:
        while results != []:
            start += step
            from_start = '&from=' + str(start)
            next_url = base_url + from_start
            results = requests.get(next_url).json()
            data += results
    if not as_dict:
        data = namedtupled.map(data)
    return data


# api v2: https://developer.usajobs.gov/Search-API/Overview

def connect(email, apikey):
    """ Forms the header parameters for authenticating with the v2 api. """
    headers = {'Host': 'data.usajobs.gov',
               'User-Agent': email,
               'Authorization-Key': apikey}
    return headers


def query(terms, auth=None, as_dict=True):
    """ Constructs v2 explicit queries with parameters outlined here:
    https://developer.usajobs.gov/Search-API/API-Query-Parameters """
    base_url = 'https://data.usajobs.gov/api/search?'
    url = base_url + terms
    if not auth:
        env = namedtupled.env(['email', 'apikey'])
        headers = connect(email=env.email, apikey=env.apikey)
    resp = requests.get(url, headers=headers)
    data = resp.json()
    if not as_dict:
        data = namedtupled.map(data)
    return data
