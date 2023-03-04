from pig import player
import pickle


class Highscore:
    def __init__(self, path):
        self._highscores = dict()
        self._path = path

    def get_highscores(self):
        # create dictionary if first time running game on new system

        with open(self._path, 'rb') as highscores_file:
            try:
                self._highscores = pickle.load(highscores_file)
            except EOFError:  # if no highscores (empty file), use empty dict
                pass

        # return table with scores from file

    def update_highscore(self, player: player.Player, won: bool):
        # check for name in file, if name is there, update highscore
        # if name is not there, add it
        self.get_highscores()
        if player.get_name() in self._highscores:
            # get wins from list stored in dict
            wins = self._highscores[player.get_name()][0]
            # get played games from list stored in dict and add 1
            games_played = self._highscores[player.get_name()][1] + 1
            if won:
                wins += 1
            # update wins and games played
            self._highscores[player.get_name()] = [wins, games_played]
        else:
            if won:
                highscore = [1, 1]  # 1 win, 1 game played
            else:
                highscore = [0, 1]  # 0 wins, 1 game played
            # add new player and games played
            self._highscores[player.get_name()] = highscore
        with open(self._path, 'wb') as highscore_file:
            pickle.dump(self._highscores, highscore_file)
        # get as string / list method
        # highscore[0] = wins, highscore[1] = games played. stored in
        # list in dict

    def __str__(self):
        highscore_string = ""
        self.get_highscores()  # Get latest highscores before printing
        for user, highscore in self._highscores.items():
            highscore_string += (
                f'Name: {user}, '
                f'Wins: {highscore[0]}, '
                f'Games played: {highscore[1]}\n'
            )
        return highscore_string
