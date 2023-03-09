import unittest
from pig.dice import Dice


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init(self):
        """"Instantiate and object and test its default value"""
        dc = Dice()
        value = dc.get_value()
        exp = 0 <= value
        self.assertTrue(exp)
    
    def test_get_value(self):
        """Instantiates object and tests getter for vaiable __value"""
        dc = Dice()
        value = dc.get_value()
        self.assertEqual(0, value)
    
    def test_roll_dice(self):
        """Rolls dice and checks that the number is within bounds"""
        dc = Dice()
        dc.roll_dice()
        exp1 = dc.get_value() >= dc.get_lower_value()
        exp2 = dc.get_value() < dc.get_higher_value()
        self.assertTrue(exp1)
        self.assertTrue(exp2)

    def test_set_value(self):
        """"Sets value of dice and verifies value"""
        dc = Dice()
        dc.set_value(4)
        exp = dc.get_value() == 4
        self.assertTrue(exp)
    
    def test_print_face(self):
        """Rolls dice and prints face"""
        dc = Dice()
        dc.roll_dice()
        dc.print_face()

if __name__ == "__main__":
    unittest.main()
