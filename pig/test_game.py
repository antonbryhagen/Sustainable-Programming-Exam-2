#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from game import Game


class TestGameClass(unittest.TestCase):
    """Test game class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Game()
        exp = Game
        self.assertIsInstance(res, exp)

    def test_player_amount(self):
        """Set player amount and check that it changes."""
        game_object = Game()
        game_object.player_amount(True)
        self.assertEqual(game_object.singleplayer, True)

    def test_player_singleplayer(self):
        """Create player and check if it is created."""
        game_object = Game()
        game_object.player_amount(True)
        game_object.player("Username")
        self.assertEqual(game_object.p_1.get_name(), "Username")

    def test_player_multiplayer(self):
        """Create two player and check if they are created."""
        game_object = Game()
        game_object.player_amount(False)
        game_object.player("Username1")
        self.assertEqual(game_object.p_1.get_name(), "Username1")
        game_object.player("Username2")
        self.assertEqual(game_object.p_2.get_name(), "Username2")

    def test_difficulty(self):
        """Set difficulty and check that it has been set."""
        game_object = Game()
        game_object.difficulty(1)
        self.assertEqual(game_object.get_difficulty(), 1)


if __name__ == "__main__":
    unittest.main()
