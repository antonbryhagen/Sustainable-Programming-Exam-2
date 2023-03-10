"""Unit testing."""

import unittest
from pig import player


class TestPlayerClass(unittest.TestCase):
    """Test Player class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = player.Player("Username")
        exp = player.Player
        self.assertIsInstance(res, exp)

    def test_get_name(self):
        """Create player and get name,check returned string is correct name."""
        test_player = player.Player("Username")
        res = test_player.get_name()
        exp = "Username"
        self.assertEqual(res, exp)

    def test_get_score(self):
        """Create player and get score, check returned score is 0."""
        test_player = player.Player("Username")
        res = test_player.get_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_name(self):
        """Create player and then set new name, check that name is updated."""
        test_player = player.Player("Username")
        test_player.set_name("Name1")
        res = test_player._name
        exp = "Name1"
        self.assertEqual(res, exp)

    def test_set_score(self):
        """Create player and then set score, check that score is updated."""
        test_player = player.Player("Username")
        test_player.set_score(5)
        res = test_player._score
        exp = 5
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
