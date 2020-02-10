import requests

class Wrapper:
    
    base_url = 'http://www.opensecrets.org/api'
    def __init__(self, apikey):
        self.api_key = apikey 

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
        
        return requests.get(f'{self.base_url}/{endpoint}', params={
            'output':'json',
            'apikey': self.api_key,
            **params}
            )
