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

  def add_player(self, name): #팀이름 알고 XP도 아니까 이름만 전
    new_player = Player(name, self.team_name) #player 생성
    self.players.append(new_player) #player를 리스트에 추가

  def del_player(self, name):
    del_player = self.return_player(name)
    self.players.remove(del_player)

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
    return total_xps

 #  def sadljkf(self, name):
 #   print(Player(name, self.team_name))
 #  실패; 같은 이름을 줘도 다르게 저장되는듯

  # team_x.players 중 한명을 print하면 class<ㅁㅇㄻㄴㄻㄹ>가 나온다
  # team_x 에 이름을 주면 해당되는놈을 삭제해주라

team_x = Team("Team X ") #Team X 생성
team_y = Team("Team Y")

team_x.add_player("nico")
team_x.add_player("lynn")

team_x.show_players()
team_x.sadljkf("nico")
team_x.show_players()

print(team_x.players)