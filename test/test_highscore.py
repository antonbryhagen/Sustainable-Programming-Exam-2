import unittest
import os

from pig import player
from pig import highscore


class TestHighscoreClass(unittest.TestCase):

    def setUp(self):  # create empty highscore file
        with open('test/highscores.bin', 'wb'):
            pass

    def test_init_default_object(self):
        # use test highscore file created
        res = highscore.Highscore('test/highscores.bin')
        exp = highscore.Highscore
        self.assertIsInstance(res, exp)

    def test_get_highscore_empty(self):
        """Test getting highscores method with empty highscore file"""
        highscore_object = highscore.Highscore('test/highscores.bin')
        highscore_object.get_highscores()
        # Should be empty dict
        self.assertEqual(highscore_object._highscores, {})

    def test_get__and_update_highscore_new_player_win(self):
        """
        Test getting and updating highscores method with highscore file for
        a new player, win
        """
        highscore_object = highscore.Highscore('test/highscores.bin')
        player_object = player.Player("Username")
        highscore_object.update_highscore(player_object, True)
        highscore_object.get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [1, 1]})

    def test_get__and_update_highscore_new_player_loose(self):
        """
        Test getting and updating highscores method with highscore file for
        a new player, loose
        """
        highscore_object = highscore.Highscore('test/highscores.bin')
        player_object = player.Player("Username")
        highscore_object.update_highscore(player_object, False)
        highscore_object.get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [0, 1]})

    def test_update_highscore(self):
        """Test updating highscore for a player"""
        highscore_object = highscore.Highscore('test/highscores.bin')
        player_object = player.Player("Username")
        highscore_object.update_highscore(player_object, True)  # First game
        highscore_object.update_highscore(player_object, True)  # Second game
        highscore_object.get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [2, 2]})

    def test_update_highscore_lost(self):
        """Test updating highscore for a player when loosing one game"""
        highscore_object = highscore.Highscore('test/highscores.bin')
        player_object = player.Player("Username")
        highscore_object.update_highscore(player_object, True)  # First game
        highscore_object.update_highscore(player_object, False)  # Second game
        highscore_object.get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [1, 2]})

    def test_str(self):
        """Test if __str__ method returns correct string"""
        highscore_object = highscore.Highscore('test/highscores.bin')
        player_object = player.Player("Username")
        highscore_object.update_highscore(player_object, True)
        exp = 'Name: Username, Wins: 1, Games played: 1\n'
        self.assertEqual(highscore_object.__str__(), exp)

    def tearDown(self):
        os.remove('test/highscores.bin')
