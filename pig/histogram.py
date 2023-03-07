"""Generate dice face occurrence histogram"""

import math

class Histogram:
    """Histogram."""

    def __init__(self):
        """Init the object."""
        self._occurrence_dict = {}
        self._percentage_dict = {}
        self._rounded_percentage_dict = {}

    def _count_occurrence(self, dice_history):
        """Calculate occurrence of dice faces from dice history."""
        self._occurrence_dict = {face: dice_history.count(face) for face in dice_history}

    def _calculate_percentage(self, dice_history):
        """Calculate ocurrence of dice face in percentage."""
        self._percentage_dict = {face: dice_history.count(face)/len(dice_history) for face in dice_history}
        for key in self._percentage_dict.keys():
            self._rounded_percentage_dict[key] = math.floor(self._percentage_dict[key]*10)

    def get_histogram(self, dice_history):
        """Get histogram as a formatted string."""
        self._count_occurrence(dice_history)
        self._calculate_percentage(dice_history)
        bar_list = ['']*6
        for i, key in enumerate(self._rounded_percentage_dict.keys()):
            bar_list[i] = '*\n'*self._rounded_percentage_dict[key]
            bar_list[i] = bar_list[i] + '*'
        return bar_list

def main():
    faces = [2, 5, 6, 2, 2, 4, 5, 5, 5, 3, 3, 3, 4]
    histo = Histogram()
    histo._count_occurrence(faces)
    histo._calculate_percentage(faces)
    print(histo._occurrence_dict)
    print(histo._percentage_dict)
    print(histo._rounded_percentage_dict)

    bars = histo.get_histogram(faces)
    print(f"{bars[0]}, {bars[1]}")

if __name__ == "__main__":
    main()