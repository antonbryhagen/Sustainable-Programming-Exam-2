"""Unit testing."""

import unittest
import os

from player import Player
from highscore import Highscore


class TestHighscoreClass(unittest.TestCase):
    """Test highscore class."""

    def setUp(self):
        """Create new highscore file for each test case."""
        with open("pig/test_highscores.bin", "wb"):
            pass

    def test_init_default_object(self):
        """Instantiate highscore object and check its properties."""
        res = Highscore("pig/test_highscores.bin")
        exp = Highscore
        self.assertIsInstance(res, exp)

    def test_get_highscore_empty(self):
        """Get highscores with empty file, check highscore dict is empty."""
        highscore_object = Highscore("pig/test_highscores.bin")
        highscore_object._get_highscores()
        self.assertEqual(highscore_object._highscores, {})

    def test_get__and_update_highscore_new_player_win(self):
        """Update highscore for new player, check highscore is added(W)."""
        highscore_object = Highscore("pig/test_highscores.bin")
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, True)
        highscore_object._get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [1, 1]})

    def test_get__and_update_highscore_new_player_loose(self):
        """Update highscore for new player, check highscore is added(L)."""
        highscore_object = Highscore("pig/test_highscores.bin")
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, False)
        highscore_object._get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [0, 1]})

    def test_update_highscore(self):
        """Update highscore twice for player, check highscores are added(W)."""
        highscore_object = Highscore("pig/test_highscores.bin")
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, True)
        highscore_object.update_highscore(player_object, True)
        highscore_object._get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [2, 2]})

    def test_update_highscore_lost(self):
        """Update highscore twice for player, check highscores are added(L)."""
        highscore_object = Highscore("pig/test_highscores.bin")
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, True)
        highscore_object.update_highscore(player_object, False)
        highscore_object._get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username": [1, 2]})

    def test_str(self):
        """Get highscore as string, check it matches expected format&stats."""
        highscore_object = Highscore("pig/test_highscores.bin")
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, True)
        exp = "Name: Username, Wins: 1, Games played: 1\n"
        self.assertEqual(highscore_object.__str__(), exp)

    def test_update_name(self):
        """Change name for player, check highscore transfer."""
        highscore_object = Highscore("pig/test_highscores.bin")
        player_object = Player("Username")
        highscore_object.update_highscore(player_object, True)
        exp = "Name: Username, Wins: 1, Games played: 1\n"
        self.assertEqual(highscore_object.__str__(), exp)
        player_object.set_name("Name")
        highscore_object.update_name("Username", "Name")
        exp = "Name: Name, Wins: 1, Games played: 1\n"
        self.assertEqual(highscore_object.__str__(), exp)

    def test_update_name_error(self):
        """Change name to existing user, check highscore doesn't transfer."""
        highscore_object = Highscore("pig/test_highscores.bin")
        player_object_1 = Player("Username")
        player_object_2 = Player("Name")
        highscore_object.update_highscore(player_object_1, True)
        highscore_object.update_highscore(player_object_2, True)
        exp = (
            "Name: Username, Wins: 1, Games played: 1\n"
            "Name: Name, Wins: 1, Games played: 1\n"
        )
        self.assertEqual(highscore_object.__str__(), exp)
        player_object_1.set_name("Name")
        highscore_object.update_name("Username", "Name")
        self.assertEqual(highscore_object.__str__(), exp)

    def tearDown(self):
        """Remove highscore file after each test case."""
        os.remove("pig/test_highscores.bin")


if __name__ == "__main__":
    unittest.main()
