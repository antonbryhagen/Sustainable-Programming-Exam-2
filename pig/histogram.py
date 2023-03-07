"""Generate dice face occurrence histogram"""


class Histogram:
    """Histogram."""

    def __init__(self):
        """Init the object."""
        self._occurrence_dict = {}

    def _count_occurrence(self, dice_history):
        """Calculate occurrence of dice faces from dice history."""
        self._occurrence_dict = {face: dice_history.count(face) for face in dice_history}


    def get_histogram(self, dice_history):
        """Get histogram as a formatted string."""
        self._count_occurrence(dice_history)
        return