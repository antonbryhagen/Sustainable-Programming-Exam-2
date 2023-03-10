"""Unit testing."""

import unittest
from dice import Dice


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init(self):
        """Instantiate and object and test its default value."""
        d_c = Dice()
        value = d_c.get_value()
        exp = 0 <= value
        self.assertTrue(exp)

    def test_get_value(self):
        """Instantiates object and tests getter for vaiable __value."""
        d_c = Dice()
        value = d_c.get_value()
        self.assertEqual(0, value)

    def test_roll_dice(self):
        """Rolls dice and checks that the number is within bounds."""
        d_c = Dice()
        d_c.roll_dice()
        exp1 = d_c.get_value() >= d_c.get_lower_value()
        exp2 = d_c.get_value() < d_c.get_higher_value()
        self.assertTrue(exp1)
        self.assertTrue(exp2)

    def test_set_value(self):
        """Sets value of dice and verifies value."""
        d_c = Dice()
        d_c.set_value(4)
        exp = d_c.get_value() == 4
        self.assertTrue(exp)

    def test_print_face_1(self):
        """Rolls dice and prints face."""
        d_c = Dice()
        d_c.set_value(1)
        d_c.print_face()
        exp = """
                 ---------
                |         |
                |    *    |
                |         |
                 ---------
                """
        self.assertEqual(d_c.output, exp)

    def test_print_face_2(self):
        """Rolls dice and prints face."""
        d_c = Dice()
        d_c.set_value(2)
        d_c.print_face()
        exp = """
                 ---------
                |  *      |
                |         |
                |      *  |
                 ---------
                """
        self.assertEqual(d_c.output, exp)

    def test_print_face_3(self):
        """Rolls dice and prints face."""
        d_c = Dice()
        d_c.set_value(3)
        d_c.print_face()
        exp = """
                 ---------
                |  *      |
                |    *    |
                |      *  |
                 ---------
                """
        self.assertEqual(d_c.output, exp)

    def test_print_face_4(self):
        """Rolls dice and prints face."""
        d_c = Dice()
        d_c.set_value(4)
        d_c.print_face()
        exp = """
                 ---------
                |  *   *  |
                |         |
                |  *   *  |
                 ---------
                """
        self.assertEqual(d_c.output, exp)

    def test_print_face_5(self):
        """Rolls dice and prints face."""
        d_c = Dice()
        d_c.set_value(5)
        d_c.print_face()
        exp = """
                 ---------
                |  *   *  |
                |    *    |
                |  *   *  |
                 ---------
                """
        self.assertEqual(d_c.output, exp)

    def test_print_face_6(self):
        """Rolls dice and prints face."""
        d_c = Dice()
        d_c.set_value(6)
        d_c.print_face()
        exp = """
                 ---------
                |  *   *  |
                |  *   *  |
                |  *   *  |
                 ---------
                """
        self.assertEqual(d_c.output, exp)


if __name__ == "__main__":
    unittest.main()
