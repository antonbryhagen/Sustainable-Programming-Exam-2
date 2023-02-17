from dice import Dice
from dice_hand import Dice_hand


def main():
    dc = Dice()
    dc.set_value(6)
    dc.print_face()
    dh = Dice_hand
    dh.add_rolled(dc)
    dh.print_hand()


if __name__ == '__main__':
    main()
