import unittest
from pig import intelligence
from pig import dice_hand


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_play(self):
        """Test play functionallity"""
        play = intelligence.Intelligence()
        dh = dice_hand.Dice_hand()
        action = play.play("1", dh, 0, 0)
        self.assertEqual(action, "roll")
