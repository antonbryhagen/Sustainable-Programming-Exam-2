#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Roll a dice, play the game."""

import time
from player import Player
from dice import Dice
from dice_hand import DiceHand
from intelligence import Intelligence
from highscore import Highscore
from histogram import Histogram


class Game:
    """Game class."""

    # pylint: disable=too-many-instance-attributes
    # Disabled since game needs many attributes to work

    def __init__(self, path):
        """Init the object."""
        self.d_c = Dice()
        self.d_h = DiceHand()
        self.singleplayer = None
        self.p_1 = Player("Temp1")
        self.p_2 = Player("Computer")
        self.p_1_turn = True
        self.created_first_player = False
        self.created_players = False
        self.diff = 1
        self.computer = Intelligence()
        self.highscore_handler = Highscore(path)
        self.histogram_handler = Histogram()
        self.started = False
        self.in_round = False
        self.game_won = False
        self.action = ""
        self.message = ""
        self.victory_message = ""

    def player_amount(self, one_player):
        """Set the player amount."""
        self.singleplayer = one_player

    def player(self, name):
        """Create new player object."""
        if not self.created_first_player:
            self.p_1 = Player(name)
            self.created_first_player = True
        elif not self.singleplayer and self.created_first_player:
            self.p_2 = Player(name)
            self.created_players = True
            self.in_round = True

    def difficulty(self, diff):
        """Set computer difficulty."""
        self.diff = diff
        self.in_round = True

    def get_difficulty(self):
        """Get the current difficulty."""
        return self.diff

    def all_faces(self):
        """Check if all dice faces are in history."""
        all_faces = True
        for face in range(1, 7):
            if face not in self.d_h.get_history():
                all_faces = False
        return all_faces

    def roll(self):
        """Roll dice and checks if a player has won."""
        self.d_c.roll_dice()
        if self.p_1_turn and not self.game_won:
            print("You rolled a:")
            self.d_c.print_face()
        elif not self.p_1_turn and not self.singleplayer and not self.game_won:
            print("You rolled a:")
            self.d_c.print_face()
        else:
            if (self.p_2.get_score() + self.d_h.get_rolled() < 100
                    and not self.game_won):
                print("Computer rolled a:")
                self.d_c.print_face()
        if self.d_c.get_value() == 1 and not self.game_won:
            self.d_h.add_history(self.d_c.get_value())
            self.d_h.clear_rolled()
            self.hold()
        else:
            self.d_h.add_rolled(self.d_c.get_value())
            self.d_h.add_history(self.d_c.get_value())
            if self.p_1_turn:
                if self.p_1.get_score() + self.d_h.get_rolled() >= 100:
                    print(f"{self.p_1.get_name()} Win")
                    if self.all_faces():
                        print(
                            self.histogram_handler.get_histogram(
                                self.d_h.get_history())
                        )
                    self.game_won = True
                    self.player_won()
                    self.highscore_handler.update_highscore(self.p_1, True)
                    self.in_round = False
                    if not self.singleplayer:
                        self.highscore_handler.update_highscore(self.p_2,
                                                                False)
            else:
                if self.p_2.get_score() + self.d_h.get_rolled() >= 100:
                    print(f"{self.p_2.get_name()} Win")
                    if self.all_faces():
                        print(
                            self.histogram_handler.get_histogram(
                                self.d_h.get_history())
                        )
                    self.game_won = True
                    self.player_won()
                    self.highscore_handler.update_highscore(self.p_1, False)
                    self.in_round = False
                    if not self.singleplayer:
                        self.highscore_handler.update_highscore(self.p_2, True)

    def hold(self):
        """Add score to players total points and changes turn."""
        if self.p_1_turn:
            self.p_1.set_score(self.p_1.get_score() + self.d_h.get_rolled())
            print(
                f"Player {self.p_1.get_name()} holds at:\
                {self.d_h.get_rolled()}"
            )
            print(
                f"Player {self.p_1.get_name()} score:\
                {self.p_1.get_score()}"
            )
            print("---------------------------")
            self.d_h.clear_rolled()
            self.p_1_turn = False
            if self.singleplayer:
                self.computer_play()
        else:
            self.p_2.set_score(self.p_2.get_score() + self.d_h.get_rolled())
            print(
                f"Player {self.p_2.get_name()} holds at:\
                {self.d_h.get_rolled()}"
            )
            print(
                f"Player {self.p_2.get_name()} score:\
                {self.p_2.get_score()}"
            )
            print("---------------------------")
            self.d_h.clear_rolled()
            self.p_1_turn = True

    def computer_play(self):
        """Call AI:s method to play and executes its instructions."""
        print("Computer playing:")
        while True:
            time.sleep(1.5)
            if self.p_2.get_score() + self.d_h.get_rolled() >= 100:
                break
            self.action = self.computer.play(
                self.diff, self.d_h, self.p_1.get_score(), self.p_2.get_score()
            )
            if self.action == "roll":
                self.roll()
            else:
                self.hold()
                self.p_1_turn = True
            if self.p_1_turn:
                break

    def rename(self, current_name, new_name):
        """Rename specified player and transfer highscore."""
        if current_name == self.p_1.get_name():
            self.p_1.set_name(new_name)
            self.highscore_handler.update_name(current_name, new_name)
        elif current_name == self.p_2.get_name():
            self.p_2.set_name(new_name)
            self.highscore_handler.update_name(current_name, new_name)
        else:
            msg = "You can only change one of the currently playing names!"
            print(msg)

    def print_menu(self):
        """Print menu."""
        self.message = """Welcome to the game!
        Type "one" to play against the computer
        Type "two" to play against a friend
        Type "highscore" to view highscores"""
        print(self.message)

    def cheat(self):
        """Set the currently playing players score to 100."""
        self.game_won = True
        if self.p_1_turn:
            self.p_1.set_score(100)
            self.roll()
        else:
            self.p_2.set_score(100)
            self.roll()

    def restart(self):
        """Reset points and history."""
        self.p_1.set_score(0)
        self.p_2.set_score(0)
        self.d_h.clear_rolled()
        self.d_h.clear_history()
        self.p_1_turn = True
        self.game_won = False

    def player_won(self):
        """Ask if player wants to play again."""
        self.victory_message = "Play again? y/n"
        print(self.victory_message)
