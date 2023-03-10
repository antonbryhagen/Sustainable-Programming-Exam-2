"""Unit testing."""

import unittest
from intelligence import Intelligence
from dice_hand import Dice_hand


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_play(self):
        """Test play functionallity."""
        play = Intelligence()
        dh = Dice_hand()
        action = play.play("1", dh, 0, 0)
        self.assertEqual(action, "roll")


if __name__ == "__main__":
    unittest.main()
