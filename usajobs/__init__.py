import requests
import namedtupled


# api v2: https://developer.usajobs.gov/Search-API/Overview
# api v3: http://search.digitalgov.gov/developer/jobs.html


def connect(email, apikey):                                            # api v2
    """ Forms the header parameters for authenticating with the v2 api. """
    headers = {'Host': 'data.usajobs.gov',
               'User-Agent': email,
               'Authorization-Key': apikey}
    return headers


def query(terms, auth=None, as_dict=True):                             # api v2
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


def search(terms, as_dict=False):                                      # api v3
    """ Constructs v3 fuzzy searches with parameters outlined here:
    http://search.digitalgov.gov/developer/jobs.html """
    words = [x for x in terms.split(' ') if x]
    blob = '+'.join(words)
    base_url = 'https://api.usa.gov/jobs/search.json?query='
    url = base_url + blob
    resp = requests.get(url)
    data = resp.json()
    if not as_dict:
        data = namedtupled.map(data)
    return data
