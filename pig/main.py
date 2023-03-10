#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main program."""

from shell import Shell


def main():
    """Execute the main program."""
    print(__doc__)
    Shell().cmdloop()


if __name__ == "__main__":
    main()
