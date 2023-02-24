import unittest
from pig import player

class TestPlayerClass(unittest.TestCase):

    def test_init_default_object(self):
        res = player.Player("Username")
        exp = player.Player
        self.assertIsInstance(res, exp)
    
    def test_get_name(self):
        test_player = player.Player("Username")
        res = test_player.get_name()
        exp = "Username"
        self.assertEqual(res, exp)

    def test_get_score(self):
        test_player = player.Player("Username")
        res = test_player.get_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_get_current_turn_score(self):
        test_player = player.Player("Username")
        res = test_player.get_current_turn_score()
        exp = 0
        self.assertEqual(res, exp)
    
    def test_set_name(self):
        test_player = player.Player("Username")
        test_player.set_name("Name1")
        res = test_player._name
        exp = "Name1"
        self.assertEqual(res, exp)

    def test_set_score(self):
        test_player = player.Player("Username")
        test_player.set_score(5)
        res = test_player._score
        exp = 5
        self.assertEqual(res, exp)

    def test_set_current_turn_score(self):
        test_player = player.Player("Username")
        test_player.set_current_turn_score(5)
        res = test_player._current_turn_score
        exp = 5
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()