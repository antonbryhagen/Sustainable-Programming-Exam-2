"""Unit testing."""

import unittest
from dice import Dice
from dice_hand import DiceHand


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init(self):
        """Instantiates object and verifies varable."""
        d_h = DiceHand()
        self.assertIsInstance(d_h, DiceHand)

    def test_add_history(self):
        """Adds dice to history and verifies its content."""
        d_h = DiceHand()
        d_h.add_history(5)
        history = d_h.get_history()
        length = len(history)
        self.assertEqual(length, 1)

    def test_clear_history(self):
        """Adds dice to history, uses clear method and verifies its empty."""
        d_h = DiceHand()
        d_c = Dice()
        d_h.add_history(d_c)
        d_h.clear_history()
        exp = d_h.get_history()
        length = len(exp)
        self.assertEqual(length, 0)

    def test_print_hand(self):
        """Rolls dice and adds object to hand then prints the hand."""
        d_h = DiceHand()
        d_c = Dice()
        d_c.roll_dice()
        d_h.add_rolled(d_c.get_value())
        d_h.print_hand()

    def test_add_rolled(self):
        """Adds dice of value 5 to hand, gets score and verifies it."""
        d_h = DiceHand()
        d_c = Dice()
        d_c.set_value(5)
        d_h.add_rolled(d_c.get_value())
        score = d_h.get_rolled()
        self.assertEqual(score, 5)

    def test_get_rolled(self):
        """Adds value to dicehand and verifies value."""
        d_h = DiceHand()
        d_h.add_rolled(5)
        value = d_h.get_rolled()
        self.assertEqual(value, 5)


if __name__ == "__main__":
    unittest.main()
