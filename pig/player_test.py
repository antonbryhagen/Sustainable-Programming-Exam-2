import player

player_one = player.Player("Anton")


print(player_one.get_name())
print(player_one.get_score())
player_one.set_score(20)
print(player_one.get_score())

