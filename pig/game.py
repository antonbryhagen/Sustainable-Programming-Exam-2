#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Guess the number I am thinking of."""
import player
import random


class Game:
    """Example of dice class."""

    low_number = 1
    high_number = 100
    the_number = None

    def __init__(self):
        """Init the object."""
        self._player_amount = None
        self.p1 = None
        self.p2 = None
        self._created_first_player = False
        self._difficulty = None
        self.created_players = False

    def player_amount(self, amount):
        """Set the player amount."""
        self._player_amount = amount

    def players(self):
        """Get player amount."""
        return self._player_amount

    def player(self, name):
        """Create new player object."""
        if not self._created_first_player:
            self.p1 = player.Player(name)
            self._created_first_player = True
        elif self._player_amount == 2 and self._created_first_player:
            self.p2 = player.Player(name)
            self.created_players = True

    def difficulty(self, diff):
        """Set computer difficulty."""
        self._difficulty = diff

    def start(self):
        """Start the game and randomize a new number."""
        self.the_number = random.randint(self.low_number, self.high_number)

    def cheat(self):
        """Get the number."""
        return self.the_number

    def low(self):
        """Get the lowest number possible."""
        return self.low_number

    def high(self):
        """Get the highest number possible."""
        return self.high_number
