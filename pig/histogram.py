"""Generate dice face occurrence histogram"""

import math

class Histogram:
    """Histogram."""

    def __init__(self):
        """Init the object."""
        self._percentage_dict = {}
        self._rounded_percentage_dict = {}


    def _calculate_percentage(self, dice_history):
        """Calculate ocurrence of dice face in percentage."""
        self._percentage_dict = {face: dice_history.count(face)/len(dice_history) for face in dice_history}
        for key in self._percentage_dict.keys():
            self._rounded_percentage_dict[key] = math.ceil(self._percentage_dict[key]*10)

    def get_histogram(self, dice_history):
        """Get histogram as a formatted string."""
        self._calculate_percentage(dice_history)
        chart = ''
        for i in range(10, 0, -1):
            row = ''
            for j in range(1, 7):
                if self._rounded_percentage_dict[j] >= i:
                    if j == 1:
                        row += f'{(i-1)*10:3}-{i*10:3}% | █'
                    else:
                        row += '█'
                else:
                    if j == 1:
                        row += f'{(i-1)*10:3}-{i*10:3}% |  '
                    else:
                        row += ' '
            chart += row + '\n'
        chart += ('-----------------------\n'
                  '    Face | 123456')

        return chart
