import unittest

from pig import player
from pig import highscore

class TestHighscoreClass(unittest.TestCase):

    def test_init_default_object(self):
        res = highscore.Highscore()
        exp = highscore.Highscore
        self.assertIsInstance(res, exp)

    def test_get_highscores(self):
        pass