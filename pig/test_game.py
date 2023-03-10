#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import os
from game import Game


class TestGameClass(unittest.TestCase):
    """Test game class."""

    def setUp(self):
        """Create new highscore file for each test case."""
        with open("pig/test_highscores.bin", "wb"):
            pass

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Game("pig/test_highscores.bin")
        exp = Game
        self.assertIsInstance(res, exp)

    def test_player_amount(self):
        """Set player amount and check that it changes."""
        game_object = Game("pig/test_highscores.bin")
        game_object.player_amount(True)
        self.assertEqual(game_object.singleplayer, True)

    def test_player_singleplayer(self):
        """Create player and check if it is created."""
        game_object = Game("pig/test_highscores.bin")
        game_object.player_amount(True)
        game_object.player("Username")
        self.assertEqual(game_object.p_1.get_name(), "Username")

    def test_player_multiplayer(self):
        """Create two player and check if they are created."""
        game_object = Game("pig/test_highscores.bin")
        game_object.player_amount(False)
        game_object.player("Username1")
        self.assertEqual(game_object.p_1.get_name(), "Username1")
        game_object.player("Username2")
        self.assertEqual(game_object.p_2.get_name(), "Username2")

    def test_difficulty(self):
        """Set difficulty and check that it has been set."""
        game_object = Game("pig/test_highscores.bin")
        game_object.difficulty(1)
        self.assertEqual(game_object.get_difficulty(), 1)

    def test_get_difficulty(self):
        """Set difficulty and verify getter."""
        game_object = Game("pig/test_highscores.bin")
        game_object.difficulty(1)
        self.assertEqual(game_object.get_difficulty(), 1)

    def test_roll(self):
        """Roll dice and verify result, verify game win is detected."""
        print("roll started")
        game_object = Game("pig/test_highscores.bin")
        game_object.roll()
        rolled = game_object.d_c.get_value()
        exp = 0 < rolled < 7
        self.assertTrue(exp)
        game_object.cheat()
        is_won = game_object.game_won
        self.assertTrue(is_won)

    def test_hold(self):
        """Add rolled to hand and verify hold adds to points, changes turn."""
        game_object = Game("pig/test_highscores.bin")
        game_object.d_h.add_rolled(10)
        game_object.hold()
        points = game_object.p_1.get_score()
        self.assertEqual(points, 10)
        self.assertFalse(game_object.p_1_turn)

    def test_computer_play(self):
        """Player calls roll and hold, verify computer rolls afterwards."""
        game_object = Game("pig/test_highscores.bin")
        game_object.singleplayer = True
        game_object.diff = "1"
        game_object.hold()
        choice = game_object.action
        if game_object.p_2.get_score() > 19:
            self.assertEqual(choice, "hold")
        else:
            self.assertEqual(choice, "roll")

    def test_rename(self):
        """Rename player 1 and verify new name."""
        game_object = Game("pig/test_highscores.bin")
        game_object.rename("Temp1", "Player1")
        new_name = game_object.p_1.get_name()
        self.assertEqual(new_name, "Player1")

    def test_print_menu(self):
        """Print menu and verify message."""
        game_object = Game("pig/test_highscores.bin")
        game_object.print_menu()
        self.assertEqual(
            game_object.message,
            """Welcome to the game!
        Type "one" to play against the computer
        Type "two" to play against a friend
        Type "highscore" to view highscores""",
        )

    def test_cheat(self):
        """Cheat and verify score."""
        game_object = Game("pig/test_highscores.bin")
        game_object.cheat()
        self.assertTrue(game_object.game_won)
        self.assertEqual(game_object.p_1.get_score(), 100)

    def test_restart(self):
        """Change variables as i a game was played, reset and verify values."""
        game_object = Game("pig/test_highscores.bin")
        game_object.p_1.set_score(1)
        game_object.p_2.set_score(1)
        game_object.d_h.add_rolled(1)
        game_object.p_1_turn = False
        game_object.restart()
        self.assertEqual(game_object.p_1.get_score(), 0)
        self.assertEqual(game_object.p_2.get_score(), 0)
        self.assertEqual(game_object.d_h.get_rolled(), 0)
        self.assertTrue(game_object.p_1_turn)

    def test_player_won(self):
        """Display end of game message and verify print."""
        game_object = Game("pig/test_highscores.bin")
        game_object.player_won()
        self.assertEqual(game_object.victory_message, "Play again? y/n")

    def tearDown(self):
        """Remove highscore file after each test case."""
        os.remove("pig/test_highscores.bin")


if __name__ == "__main__":
    unittest.main()
