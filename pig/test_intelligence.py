"""Unit testing."""

import unittest
from intelligence import Intelligence
from dice_hand import DiceHand


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init(self):
        """Init the object."""
        a_i = Intelligence()
        self.assertIsInstance(a_i, Intelligence)

    def test_play(self):
        """Test play functionallity."""
        play = Intelligence()
        d_h = DiceHand()
        action = play.play("1", d_h, 0, 0)
        self.assertEqual(action, "roll")

    def test_play_one(self):
        """Test play with difficulty 1."""
        play = Intelligence()
        d_h = DiceHand()
        d_h.add_rolled(0)
        action = play.play_dif_1(d_h)
        self.assertEqual(action, "roll")

    def test_play_two(self):
        """Test play with difficulty 2."""
        play = Intelligence()
        d_h = DiceHand()
        d_h.add_rolled(0)
        action = play.play_dif_1(d_h)
        self.assertEqual(action, "roll")

    def test_play_three(self):
        """Test play with difficulty 3."""
        play = Intelligence()
        d_h = DiceHand()
        d_h.add_rolled(0)
        action = play.play_dif_3(d_h, 0, 0)
        self.assertEqual(action, "roll")
        action = play.play_dif_3(d_h, 80, 0)
        self.assertEqual(action, "roll")
        d_h.add_rolled(50)
        action = play.play_dif_3(d_h, 0, 0)
        self.assertEqual(action, "hold")


if __name__ == "__main__":
    unittest.main()
