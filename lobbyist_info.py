from wrappers import Wrapper

def get_all_lobbyists(official_id, cycle=None, api_key=None):
    """
     https://www.opensecrets.org/api/?method=candContrib&cid=N00007360&cycle=2020&apikey=__apikey__
     """
    if cycle is None:
        cycle = 2020 # I don't actually know how the cycles work; I assume you can't just take the current year? 
    # if API key none, get it from some sort of appwide config defined above
    w = Wrapper(api_key)

    return w.get({'method':'candContrib', 'cid': official_id, 'cycle': cycle})


