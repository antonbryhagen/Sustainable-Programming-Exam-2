import unittest
from pig import dice
from pig import dice_hand


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init(self):
        """Instantiates object and verifies varable"""
        dh = dice_hand.Dice_hand()
        self.assertIsInstance(dh, dice_hand.Dice_hand)
    
    def test_add_rolled(self):
        """Adds die to hand and verifies content of hand"""
        dh = dice_hand.Dice_hand()
        dc = dice.Dice()
        dh.add_rolled(dc)
        r = dh.get_rolled()
        exp = isinstance(r, dice.Dice)
        self.assertTrue(exp)
    
    def test_clear_rolled(self):
        """Adds dice to hand, uses clear method and verifieshan is empty"""
        dh = dice_hand.Dice_hand()
        dc = dice.Dice()
        dh.add_rolled(dc)
        dh.clear_rolled()
        exp = dh.get_rolled()
        self.assertEqual(exp, 0)
    
    def test_print_hand(self):
        """Rolls dice and adds object to hand then prints the hand"""
        dh = dice_hand.Dice_hand()
        dc = dice.Dice()
        dc.roll_dice()
        dh.add_rolled(dc)
        dh.print_hand()
    
    def test_get_score(self):
        """Adds dice of value 5 to hand, gets score and verifies it"""
        dh = dice_hand.Dice_hand()
        dc = dice.Dice()
        dc.set_value(5)
        dh.add_rolled(dc)
        score = dh.get_score()
        self.assertEqual(score, 5)

if __name__ == "__main__":
    unittest.main()
