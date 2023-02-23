import unittest
from pig import player

class TestPlayerClass(unittest.TestCase):

    def test_init_default_object(self):
        res = player.Player("Username")
        exp = player.Player
        self.assertIsInstance(res, exp)


if __name__ == "__main__":
    unittest.main()