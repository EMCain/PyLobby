import requests

class APIError(Exception):
    def __init__(self, response):
        self.message = f'Request to {response.url} returned {response.status_code}: {response._content}'

    def __str__(self):
        return self.message

class Wrapper:
    base_url = 'http://www.opensecrets.org/api'
    def __init__(self, api_key):
        self.api_key = api_key 

    def get(self, params, endpoint=None): 
        """
        Seems you generally pass in the method as one of the params, instead of as an URL path.
        Example:

        resp = w.get({'method': 'getLegislators', 'id': 'OR'})
        based on https://www.opensecrets.org/api/?method=getLegislators&output=doc

        returns a response object; you can access the data with resp.json() (returns a dict)
        """
        if endpoint is None:
            endpoint = ''

        results = requests.get(f'{self.base_url}/{endpoint}', params={
            'output':'json',
            'apikey': self.api_key,
            **params}
        )

        if results.status_code == 200: 
            return results.json()
        else: 
            raise APIError(results)
