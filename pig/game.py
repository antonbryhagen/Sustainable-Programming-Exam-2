#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Guess the number I am thinking of."""
import random

import player
import dice
import dice_hand
import intelligence
import highscore


class Game:
    """Game class."""

    def __init__(self):
        """Init the object."""
        self.dc = dice.Dice()
        self.dh = dice_hand.Dice_hand()
        self.singleplayer = True
        self.p_1 = player.Player("Temp1")
        self.p_2 = player.Player("Temp2")
        self.p_1_turn = True
        self._created_first_player = False
        self.created_players = False
        self._difficulty = 1
        self.computer = intelligence.Intelligence()
        self.highscore_handler = highscore.Highscore('pig/highscores.bin')

    def player_amount(self, one_player):
        """Set the player amount."""
        self.singleplayer = one_player

    def player(self, name):
        """Create new player object."""
        if not self._created_first_player:
            self.p_1 = player.Player(name)
            self._created_first_player = True
        elif not self.singleplayer and self._created_first_player:
            self.p_2 = player.Player(name)
            self.created_players = True

    def difficulty(self, diff):
        """Set computer difficulty."""
        self._difficulty = diff
    
    def roll(self):
        self.dc.roll_dice()
        if self.dc.get_value() == 1:
            self.dh.clear_rolled()
            self.hold()
        else:
            self.dh.add_rolled(self.dc.get_value())
            if self.p_1_turn:
                if self.p_1.get_score() + self.dc.get_value() >= 100:
                    print("P1 Win")
            else:
                if self.p_2.get_score() + self.dc.get_value() >= 100:
                    print("P2 Win")    
    def hold(self):
        if self.p_1_turn:
            self.p_1.set_score(self.p_1.get_score() + self.dh.get_rolled())
            print(f"Player 1 holds at: {self.dh.get_rolled()}")
            self.dh.clear_rolled()
            self.p_1_turn = False
            if self.singleplayer:
                self.computer_play()
                self.p_1_turn = True
        else:
            self.p_2.set_score(self.p_2.get_score() + self.dh.get_rolled())
            print(f"Player 2 holds at: {self.dh.get_rolled()}")
            self.dh.clear_rolled()
            self.p_1_turn = True

    def computer_play(self):
        self.computer.play(self.difficulty, self.dh, self)
    
    def rename(self, current_name, new_name):
        """Rename specified player and transfer highscore."""
        if current_name == self.p_1.get_name():
            self.p_1.set_name(new_name)
            self.highscore_handler.update_name(current_name, new_name)
        elif current_name == self.p_2.get_name():
            self.p_2.set_name(new_name)
            self.highscore_handler.update_name(current_name, new_name)