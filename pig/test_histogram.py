"""Unit testing"""

import unittest
from pig import histogram


class TestHistogram(unittest.TestCase):
    """Test histogram class"""

    def test_init_default_object(self):
        """Instantiate histogram object and check its properties."""
        res = histogram.Histogram()
        exp = histogram.Histogram
        self.assertIsInstance(res, exp)
        percentage_dict_res = res._percentage_dict
        rounded_percentage_dict_res = res._rounded_percentage_dict
        self.assertDictEqual(percentage_dict_res, {})
        self.assertDictEqual(rounded_percentage_dict_res, {})
    
    def test_calculate_percentage(self):
        """
        Create histogram object and Calculate percentage and rounded percentage, 
        check that dictionary with calculated values match with dictionary with 
        correct percentages
        """
        histogram_object = histogram.Histogram()
        dice_faces = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 6]
        histogram_object._calculate_percentage(dice_faces)
        expected_percentage_dict = {1:0.09090909090909091, 
                                    2: 0.18181818181818182, 
                                    3: 0.09090909090909091, 
                                    4: 0.18181818181818182, 
                                    5: 0.18181818181818182, 
                                    6: 0.2727272727272727}
        expected_rounded_percentage_dict = {1: 1, 2: 2, 3: 1, 4: 2, 5: 2, 6: 3}
        self.assertDictEqual(histogram_object._percentage_dict, expected_percentage_dict)
        self.assertDictEqual(histogram_object._rounded_percentage_dict, 
                             expected_rounded_percentage_dict)

    def test_get_histogram(self):
        """
        Create histogram object and get histogram from dice face history, check
        that returned string is matching expected histogram
        """
        histogram_object = histogram.Histogram()
        dice_faces = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 6]
        res = histogram_object.get_histogram(dice_faces)
        exp = (" 90-100% |"
               " 80- 90% |"
               " 30- 40% |"
               " 20- 30% |      █"
               " 10- 20% |  █ ███"
               "  0- 10% | ██████"
               "-----------------------"
               "    Face | 123456")
        self.assertEqual(res, exp)

if __name__ == "__main__":
    unittest.main()
