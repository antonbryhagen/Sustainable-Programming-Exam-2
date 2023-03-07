#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a game of pig.

Take turns rolling a dice.

You can roll as many times as you want each turn or choose to hold.

If you roll a "1" your turn ends and you loose all points for that turn.

First to 100 points win.
"""

import shell


def main():
    """Execute the main program."""
    print(__doc__)
    shell.Shell().cmdloop()


if __name__ == "__main__":
    main()
