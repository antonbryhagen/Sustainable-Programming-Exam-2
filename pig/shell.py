#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import game


class Shell(cmd.Cmd):
    """Shell class with commands to run the game."""

    intro = (
        "Welcome to the Pig, the dice game. Type help or ? to list commands.\n"
        "Type rules to view the rules or type start to start the game"
    )
    prompt = "(game) "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()
    
    def do_rules(self, _):
        """Print the rules of the game."""
        rules = (
            """This is a game of pig.

Take turns rolling a dice.

You can roll as many times as you want each turn or choose to hold.

If you roll a "1" your turn ends and you loose all points for that turn.

First to 100 points win.""")
        print(rules)

    def do_start(self, _):
        """Start the game."""
        self.game.print_menu()
    
    def do_cheat(self, _):
        """Cheats"""
        print("You cheated!")
        if self.game.p_1_turn:
            self.game.p_1.set_score(100)
            self.game.roll()
        else:
            self.game.p_2.set_score(100)
            self.game.roll()

    def do_restart(self, _):
        """Whipes player points and starts game from beginning"""
        print("Resetting game")
        self.game.p_1.set_score(0)
        self.game.p_2.set_score(0)
        self.game.dh.clear_rolled()
        self.game.dh.clear_history()
        self.game.p_1_turn = True

    def do_one(self, _):
        """Select one player mode."""
        self.game.player_amount(True)
        print("Type 'player name' to set username")

    def do_two(self, _):
        """Select two player mode."""
        self.game.player_amount(False)
        print("Type 'player name' to set username")

    def do_player(self, arg):
        """Enter a player name."""
        self.game.player(arg)
        print(f'Welcome {arg}')
        if not self.game.singleplayer and not self.game.created_players:
            print("Type 'player name' to set second players username")

    def do_difficulty(self, arg):
        """Select game difficulty when playing against computer."""
        self.game.difficulty(arg)

    def do_roll(self, _):
        self.game.roll()

    def do_hold(self, _):
        """Do a guess of a number."""
        self.game.hold()

    def do_rename(self, arg1, arg2):
        """Rename specified player."""
        self.game.rename(arg1, arg2)

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Bye bye - see ya soon again")
        return True

    def do_quit(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_q(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
