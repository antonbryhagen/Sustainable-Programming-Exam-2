import unittest
from pig import dice


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init(self):
        """"Instantiate and object and test its default value"""
        dice = dice.Dice()