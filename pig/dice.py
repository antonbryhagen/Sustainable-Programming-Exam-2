"""Manage dice."""

import random


class Dice:
    """Dice class."""

    def __init__(self):
        """Init the object."""
        self.__value = 0
        self.output = ""
        self.__lower_value = 1
        self.__higher_value = 7

    def get_value(self):
        """Return value of dice."""
        return self.__value

    def roll_dice(self):
        """Roll dice."""
        self.__value = random.randrange(self.__lower_value,
                                        self.__higher_value)

    def get_higher_value(self):
        """Return maximum posssible result of roll."""
        return self.__higher_value

    def get_lower_value(self):
        """Return minimum possible result of roll."""
        return self.__lower_value

    def set_value(self, new_value):
        """Set value of dice."""
        self.__value = new_value
        print(self.__value)

    def print_face(self):
        """Print face of dice."""
        if self.__value != 0:
            if self.__value == 1:
                self.output = """
                 ---------
                |         |
                |    *    |
                |         |
                 ---------
                """
            elif self.__value == 2:
                self.output = """
                 ---------
                |  *      |
                |         |
                |      *  |
                 ---------
                """
            elif self.__value == 3:
                self.output = """
                 ---------
                |  *      |
                |    *    |
                |      *  |
                 ---------
                """
            elif self.__value == 4:
                self.output = """
                 ---------
                |  *   *  |
                |         |
                |  *   *  |
                 ---------
                """
            elif self.__value == 5:
                self.output = """
                 ---------
                |  *   *  |
                |    *    |
                |  *   *  |
                 ---------
                """
            else:
                self.output = """
                 ---------
                |  *   *  |
                |  *   *  |
                |  *   *  |
                 ---------
                """
            print(self.output)
