import unittest
from pig.dice import Dice
from pig.dice_hand import Dice_hand


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init(self):
        """Instantiates object and verifies varable"""
        dh = Dice_hand()
        self.assertIsInstance(dh, Dice_hand)
    
    def test_add_rolled(self):
        """Adds die to hand and verifies content of hand"""
        dh = Dice_hand()
        dc = Dice()
        dh.add_rolled(dc)
        r = dh.get_rolled()
        exp = isinstance(r, Dice)
        self.assertTrue(exp)
    
    def test_clear_rolled(self):
        """Adds dice to hand, uses clear method and verifieshan is empty"""
        dh = Dice_hand()
        dc = Dice()
        dh.add_rolled(dc)
        dh.clear_rolled()
        exp = dh.get_rolled()
        self.assertEqual(exp, 0)
    
    def test_print_hand(self):
        """Rolls dice and adds object to hand then prints the hand"""
        dh = Dice_hand()
        dc = Dice()
        dc.roll_dice()
        dh.add_rolled(dc)
        dh.print_hand()
    
    def test_get_score(self):
        """Adds dice of value 5 to hand, gets score and verifies it"""
        dh = Dice_hand()
        dc = Dice()
        dc.set_value(5)
        dh.add_rolled(dc)
        score = dh.get_score()
        self.assertEqual(score, 5)

if __name__ == "__main__":
    unittest.main()
