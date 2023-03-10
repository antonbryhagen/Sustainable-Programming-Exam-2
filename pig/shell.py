#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
from game import Game


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
        self.game = Game("pig/highscores.bin")

    def do_rules(self, _):
        """Print the rules of the game."""
        rules = """This is a game of pig.

            Take turns rolling a dice.

            You can roll as many times as you want each turn or choose to hold.


            If you roll a "1" your turn ends and you loose all points for that
            turn.

            First to 100 points win."""
        print(rules)

    def do_start(self, _):
        """Start the game."""
        if not self.game.started:
            self.game.print_menu()
            self.game.started = True
        else:
            print("Already started the game.")

    def do_cheat(self, _):
        """Cheat."""
        if self.game.in_round:
            print("You cheated!")
            self.game.cheat()
        else:
            print("Currently not playing.")

    def do_restart(self, _):
        """Whipe player points and starts game from beginning."""
        if self.game.in_round:
            print("Resetting game")
            self.game.restart()
        else:
            print("Currently not playing.")

    def do_one(self, _):
        """Select one player mode."""
        if self.game.singleplayer is None and self.game.started:
            self.game.player_amount(True)
            print("Type 'player name' to set username")
        elif not self.game.started:
            print("Start the game before selecting player amount.")
        else:
            print("Already selected player amount.")

    def do_two(self, _):
        """Select two player mode."""
        if self.game.singleplayer is None and self.game.started:
            self.game.player_amount(False)
            print("Type 'player name' to set username")
        elif not self.game.started:
            print("Start the game before selecting player amount.")
        else:
            print("Already selected player amount.")

    def do_player(self, arg):
        """Enter a player name."""
        if (self.game.singleplayer and not self.game.created_first_player) or (
            not self.game.singleplayer and not self.game.created_players
        ):
            if not arg:
                print("Missing argument, try player TestUser")
            else:
                self.game.player(arg)
                print(f"Welcome {arg}")
                if self.game.singleplayer:
                    print("Type 'difficulty 1, 2 or 3' to select difficulty")
                if (not self.game.singleplayer
                        and not self.game.created_players):
                    print("Type 'player name' to set second players username")
                if not self.game.singleplayer and self.game.created_players:
                    print("Type 'roll' to roll the dice and 'hold' to end "
                          "your turn")
        else:
            print("Already created player(s).")

    def do_difficulty(self, arg):
        """Select game difficulty when playing against computer."""
        if self.game.singleplayer and self.game.created_first_player:
            if "3" >= arg >= "1":
                self.game.difficulty(arg)
                print("Type 'roll' to roll the dice and 'hold' to end your "
                      "turn")
            else:
                print("Enter a valid difficulty: 1, 2 or 3")
        else:
            print("Unable to change difficulty.")

    def do_roll(self, _):
        """Roll the dice."""
        if self.game.in_round:
            self.game.roll()
        else:
            print("Currently not playing.")

    def do_hold(self, _):
        """Hold current hand."""
        if self.game.in_round:
            self.game.hold()
        else:
            print("Currently not playing.")

    def do_rename(self, arg1):
        """Rename specified player."""
        if (
            self.game.created_first_player or self.game.created_players
        ) and not self.game.in_round:
            if (not arg1) or (" " not in arg1):
                print("Missing argument, try rename TestUser User")
            else:
                arg2 = arg1.split()[1]
                arg1 = arg1.split()[0]
                self.game.rename(arg1, arg2)
        elif self.game.in_round:
            print("Can't rename while in-game.")
        else:
            print("There are currently no players to rename.")

    def do_highscore(self, _):
        """View highscore list."""
        if not self.game.in_round and self.game.started:
            print(self.game.highscore_handler)

    def do_y(self, _):
        """Restart game from beginning."""
        self.game.restart()
        self.game.singleplayer = None
        self.game.created_first_player = False
        self.game.created_players = False
        self.game.in_round = False
        self.game.print_menu()

    def do_n(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_exit(self, _):
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
