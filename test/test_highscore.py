import unittest
import os

from pig import player
from pig import highscore

class TestHighscoreClass(unittest.TestCase):

    def setUp(self): # create empty highscore file
        with open('test/highscores.bin', 'wb') as create_highscore_file:
            pass

    def test_init_default_object(self):
        res = highscore.Highscore('test/highscores.bin') # use test highscore file created
        exp = highscore.Highscore
        self.assertIsInstance(res, exp)

    def test_get_highscore_empty(self):
        """Test getting highscores method with empty highscore file"""
        highscore_object = highscore.Highscore('test/highscores.bin')
        highscore_object.get_highscores()
        self.assertEqual(highscore_object._highscores, {}) #Should be empty dict

    def test_get_highscore(self):
        pass

    def test_update_highscore_new_player(self):
        pass

    def test_update_highscore_(self):
        pass
    

    def tearDown(self):
        os.remove('test/highscores.bin')