from unittest import TestCase
import os
from os.path import join, dirname
from dotenv import load_dotenv

from wrappers import Wrapper
from lobbyist_info import get_all_lobbyists

# Create .env file path.
dotenv_path = join(dirname(__file__), '../.env')
 
# Load file from the path.
load_dotenv(dotenv_path)

API_KEY = os.getenv('api_key')

class LobbyistInfoTest(TestCase):
    def test_get_all_lobbyists_gets_multiple(self):
        # when the user passes an elected official's ID into get_all_lobbyists, it should return some list of lobbyists. 
        official_id = None 
        all_lobbyists = get_all_lobbyists(official_id, api_key=API_KEY)
        self.assertTrue(all_lobbyists, msg="list should not be empty")
        pass 
