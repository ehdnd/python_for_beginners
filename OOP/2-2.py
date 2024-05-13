class Player:

  def __init__(self, name, team):
    self.name = name
    self.xp = 1500
    self.team = team

  def introduce(self):
    print(f"Hello! I am {self.name} and I play for {self.team}")


class Team:

  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []

  def add_player(self, name):
    new_player = Player(name, self.team_name)
    self.players.append(new_player)

  def del_player(self, name):
    del_player = self.return_player(name)
    self.players.remove(del_player)
    print(f"{del_player.name} has been removed from {del_player.team}.")

  def return_player(self, name):
    for player in self.players:
      if name == player.name:
        return player

  def show_players(self):
    for player in self.players:
      player.introduce()

  def total_xps(self):
    total_xps = 0
    for player in self.players:
      total_xps += player.xp
    print(f"{self.team_name}'s total xps are {total_xps}")


team_x = Team("Team X ")
team_y = Team("Team Y")

team_x.add_player("nico")
team_x.add_player("lynn")
team_x.add_player("taeung")

team_x.show_players()
team_x.del_player("nico")
team_x.show_players()

team_x.total_xps()