import unittest
import os
import pickle

from pig import player
from pig import highscore

class TestHighscoreClass(unittest.TestCase):

    def setUp(self): # create empty highscore file
        with open('test/highscores.bin', 'wb') as create_highscore_file:
            pass

    def test_init_default_object(self):
        res = highscore.Highscore('test/highscores.bin') # use test highscore file created
        exp = highscore.Highscore
        self.assertIsInstance(res, exp)

    def test_get_highscore_empty(self):
        """Test getting highscores method with empty highscore file"""
        highscore_object = highscore.Highscore('test/highscores.bin')
        highscore_object.get_highscores()
        self.assertEqual(highscore_object._highscores, {}) #Should be empty dict

    def test_get__and_update_highscore_new_player(self):
        """Test getting and updating highscores method with highscore file for a new player"""
        highscore_object = highscore.Highscore('test/highscores.bin')
        player_object = player.Player("Username")
        highscore_object.update_highscore(player_object, True)
        highscore_object.get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username" : [1,1]}) #Should be empty dict

    def test_update_highscore(self):
        """Test updating highscore for a player"""
        highscore_object = highscore.Highscore('test/highscores.bin')
        # Make sure highscore file is empty / contains empty dictionary
        with open('test/highscores.bin', 'wb') as bin_file:
            try:
                pickle.dump({}, bin_file)
            except IOError:
                print("Error emptying mock file")

        player_object = player.Player("Username")
        highscore_object.update_highscore(player_object, True) # First game
        highscore_object.update_highscore(player_object, True) # Second game
        highscore_object.get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username" : [2, 2]})

    def test_update_highscore_lost(self):
        """Test updating highscore for a player when loosing one game"""
        highscore_object = highscore.Highscore('test/highscores.bin')
        # Make sure highscore file is empty / contains empty dictionary
        with open('test/highscores.bin', 'wb') as bin_file:
            try:
                pickle.dump({}, bin_file)
            except IOError:
                print("Error emptying mock file")

        player_object = player.Player("Username")
        highscore_object.update_highscore(player_object, True) # First game
        highscore_object.update_highscore(player_object, False) # Second game
        highscore_object.get_highscores()
        self.assertEqual(highscore_object._highscores, {"Username" : [2, 1]})
    
    def test_str(self):
        """Test if __str__ method returns correct string"""
        highscore_object = highscore.Highscore('test/highscores.bin')
        player_object = player.Player("Username")
        highscore_object.update_highscore(player_object, True)
        self.assertEqual(highscore_object.__str__(), 'Name: Username, Wins: 1, Games played: 1\n')       

    def tearDown(self):
        os.remove('test/highscores.bin')