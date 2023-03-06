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
    """Example of class with command actions to roll a dice."""

    intro = (
        "Welcome to the game. Type help or ? to list commands.\n"
        "Type start to start"
    )
    prompt = "(game) "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()

    def do_start(self, _):
        """Start the game."""
        msg = (
            "Please select how many players, type one for one player, "
            "or two for two players"
        )
        print(msg)

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
        print(self.game.dc.get_value())

    def do_hold(self, _):
        """Do a guess of a number."""
        msg = "You chose to hold"
        self.game.hold()
        print(msg)

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
