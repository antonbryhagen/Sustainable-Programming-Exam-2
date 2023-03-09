import unittest
from pig import dice
from pig import dice_hand


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init(self):
        """Instantiates object and verifies varable"""
        dh = dice_hand.Dice_hand()
        self.assertIsInstance(dh, dice_hand.Dice_hand)

    def test_add_history(self):
        """Adds dice to history and verifies its content"""
        dh = dice_hand.Dice_hand()
        dh.add_history(5)
        r = dh.get_history()
        length = len(r)
        self.assertEqual(length, 1)

    def test_clear_history(self):
        """Adds dice to history, uses clear method and verifies its empty"""
        dh = dice_hand.Dice_hand()
        dc = dice.Dice()
        dh.add_history(dc)
        dh.clear_history()
        exp = dh.get_history()
        length = len(exp)
        self.assertEqual(length, 0)

    def test_print_hand(self):
        """Rolls dice and adds object to hand then prints the hand"""
        dh = dice_hand.Dice_hand()
        dc = dice.Dice()
        dc.roll_dice()
        dh.add_rolled(dc.get_value())
        dh.print_hand()

    def test_add_rolled(self):
        """Adds dice of value 5 to hand, gets score and verifies it"""
        dh = dice_hand.Dice_hand()
        dc = dice.Dice()
        dc.set_value(5)
        dh.add_rolled(dc.get_value())
        score = dh.get_rolled()
        self.assertEqual(score, 5)

    def test_get_rolled(self):
        """Adds value to dicehand and verifies value"""
        dh = dice_hand.Dice_hand()
        dh.add_rolled(5)
        value = dh.get_rolled()
        self.assertEqual(value, 5)
