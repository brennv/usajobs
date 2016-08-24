import requests


def connect(email, apikey):
    headers = {'Host': 'data.usajobs.gov', 'User-Agent': email,
               'Authorization-Key': apikey}
    return headers
