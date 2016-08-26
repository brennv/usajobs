import requests
import namedtupled
import time
# api v3: http://search.digitalgov.gov/developer/jobs.html


def search(terms, start=0, step=100, as_dict=False, sleep=0.1, data=[]):
    """ Constructs v3 fuzzy searches with parameters outlined here:
    http://search.digitalgov.gov/developer/jobs.html """
    base_url = 'https://api.usa.gov/jobs/search.json?'
    words = [x for x in terms.split(' ') if x]
    query = 'query=' + '+'.join(words)
    size = '&size=' + str(step)
    _from = '&from=' + str(start)
    url = base_url + query + size + _from
    response = requests.get(url)
    results = response.json()
    if not as_dict:
        results = namedtupled.map(results)
    data += results
    print(len(data), end='\r')
    if len(results) == step:
        _next = start + step
        time.sleep(sleep)
        search(terms=terms, start=_next, step=step, as_dict=as_dict,
               sleep=sleep, data=data)
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
