"""Unit testing."""

import unittest
from dice import Dice
from dice_hand import Dice_hand


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init(self):
        """Instantiates object and verifies varable."""
        dh = Dice_hand()
        self.assertIsInstance(dh, Dice_hand)

    def test_add_history(self):
        """Adds dice to history and verifies its content."""
        dh = Dice_hand()
        dh.add_history(5)
        r = dh.get_history()
        length = len(r)
        self.assertEqual(length, 1)

    def test_clear_history(self):
        """Adds dice to history, uses clear method and verifies its empty."""
        dh = Dice_hand()
        dc = Dice()
        dh.add_history(dc)
        dh.clear_history()
        exp = dh.get_history()
        length = len(exp)
        self.assertEqual(length, 0)

    def test_print_hand(self):
        """Rolls dice and adds object to hand then prints the hand."""
        dh = Dice_hand()
        dc = Dice()
        dc.roll_dice()
        dh.add_rolled(dc.get_value())
        dh.print_hand()

    def test_add_rolled(self):
        """Adds dice of value 5 to hand, gets score and verifies it."""
        dh = Dice_hand()
        dc = Dice()
        dc.set_value(5)
        dh.add_rolled(dc.get_value())
        score = dh.get_rolled()
        self.assertEqual(score, 5)

    def test_get_rolled(self):
        """Adds value to dicehand and verifies value."""
        dh = Dice_hand()
        dh.add_rolled(5)
        value = dh.get_rolled()
        self.assertEqual(value, 5)


if __name__ == "__main__":
    unittest.main()
