"""Unit testing"""

import unittest
import os

from pig.player import Player
from pig.highscore import Highscore


class TestHighscoreClass(unittest.TestCase):
    """Test highscore class"""

    def setUp(self):
        """Create new highscore file for each test case."""
        with open('test/highscores.bin', 'wb'):
            pass

    def test_init_default_object(self):
        """Instantiate highscore object and check its properties."""
        res = Highscore('test/highscores.bin')
        exp = Highscore
        self.assertIsInstance(res, exp)

    def test_get_highscore_empty(self):
        """Get highscores from empty file and check highscore dictionary is empty."""
        highscore_object = Highscore('test/highscores.bin')
        highscore_object._get_highscores()
        self.assertEqual(highscore_object._highscores, {})

    def test_get__and_update_highscore_new_player_win(self):
        """
        Update highscore for a new player and get updated highscore, check highscore
        dictionary contains the new player with one game played and one win.
        """
        highscore_object = Highscore('test/highscores.bin')
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, True)
        highscore_object._get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [1, 1]})

    def test_get__and_update_highscore_new_player_loose(self):
        """
        Update highscore for a new player and get updated highscore, check highscore
        dictionary contains the new player with one game played and zero win.
        """
        highscore_object = Highscore('test/highscores.bin')
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, False)
        highscore_object._get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [0, 1]})

    def test_update_highscore(self):
        """
        Update highscore twice for a player and get highscore, check highscore 
        dictionary contains the recurring player with 2 games played and 2 wins
        """
        highscore_object = Highscore('test/highscores.bin')
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, True)
        highscore_object.update_highscore(player_object, True)
        highscore_object._get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [2, 2]})

    def test_update_highscore_lost(self):
        """
        Update highscore twice for a player and get highscore, check highscore 
        dictionary contains the recurring player with 2 games played and 1 win
        """
        highscore_object = Highscore('test/highscores.bin')
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, True)
        highscore_object.update_highscore(player_object, False)
        highscore_object._get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [1, 2]})

    def test_str(self):
        """
        Get string representation of highscore object and check that the string
        match expected format and statistics
        """
        highscore_object = Highscore('test/highscores.bin')
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, True)
        exp = 'Name: Username, Wins: 1, Games played: 1\n'
        self.assertEqual(highscore_object.__str__(), exp)

    def test_update_name(self):
        """
        Update highscore and change username, check that highscore transferred
        to the new name
        """
        highscore_object = Highscore('test/highscores.bin')
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, True)
        exp = 'Name: Username, Wins: 1, Games played: 1\n'
        self.assertEqual(highscore_object.__str__(), exp)
        player_object.set_name("Name")
        highscore_object.update_name("Username", "Name")
        exp = 'Name: Name, Wins: 1, Games played: 1\n'
        self.assertEqual(highscore_object.__str__(), exp)
    
    def test_update_name_error(self):
        """
        Update highscore and change username to already existing username, check that
        highscore doesn't transfer to already existing user
        """
        highscore_object = Highscore('test/highscores.bin')
        player_object_1 = Player("Username")
        player_object_2 = Player("Name")
        highscore_object.update_highscore(player_object_1, True)
        highscore_object.update_highscore(player_object_2, True)
        exp = ('Name: Username, Wins: 1, Games played: 1\n'
               'Name: Name, Wins: 1, Games played: 1\n')
        self.assertEqual(highscore_object.__str__(), exp)
        player_object_1.set_name("Name")
        highscore_object.update_name("Username", "Name")
        self.assertEqual(highscore_object.__str__(), exp)

    def tearDown(self):
        """Remove highscore file after each test case"""
        os.remove('test/highscores.bin')

if __name__ == "__main__":
    unittest.main()
