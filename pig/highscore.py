"""Keep track of highscores."""


import pickle
from pig import player


class Highscore:
    """Highscore class."""

    def __init__(self, path):
        """Init the object."""
        self._highscores = {}
        self._path = path

    def _get_highscores(self):
        """Load highscore dictionary from highscore file."""
        with open(self._path, 'rb') as highscores_file:
            try:
                self._highscores = pickle.load(highscores_file)
            except EOFError:
                pass

    def update_highscore(self, user: player.Player, won: bool):
        """Update highscore dictionary and write to highscore file."""
        self._get_highscores()
        # dictionary -> {name: [wins, games_played]}
        if user.get_name() in self._highscores:
            wins = self._highscores[user.get_name()][0]
            games_played = self._highscores[user.get_name()][1] + 1
            if won:
                wins += 1
            self._highscores[user.get_name()] = [wins, games_played]
        else:
            if won:
                highscore = [1, 1]
            else:
                highscore = [0, 1]
            self._highscores[user.get_name()] = highscore

        with open(self._path, 'wb') as highscore_file:
            pickle.dump(self._highscores, highscore_file)

    def __str__(self):
        """Get highscores as a formatted string."""
        highscore_string = ""
        self._get_highscores()  # Get latest highscores before printing
        for user, highscore in self._highscores.items():
            highscore_string += (
                f'Name: {user}, '
                f'Wins: {highscore[0]}, '
                f'Games played: {highscore[1]}\n'
            )
        return highscore_string
