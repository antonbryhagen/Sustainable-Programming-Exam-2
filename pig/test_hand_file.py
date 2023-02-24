from dice import Dice
from dice_hand import Dice_hand


def main():
    dc = Dice()
    dc.set_value(6)
    dc.print_face()
    dh = Dice_hand()
    dh.add_rolled(dc)
    dh.print_hand()

    dc2 = Dice()
    dc2.set_value(4)
    dc2.print_face()
    dh.add_rolled(dc2)
    dh.print_hand()

    score = dh.get_score()
    print("Score: " + str(score))


if __name__ == '__main__':
    main()
