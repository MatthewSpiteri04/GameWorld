from models.player import RockPaperScissorsPlayer

class Game:
    def __init__(self, id, players):
        self.id = id
        self.players = players


class RockPaperScissors(Game):
    def __init__(self, id, players):
        super().__init__(id, players)
        self.player1 = None
        self.player2 = None
        self.choices = ["Rock", "Paper", "Scissors"]
    
    def assign_players(self):
        if len(self.players) == 2:
            self.player1 = RockPaperScissorsPlayer.from_player(self.players[0])
            self.player2 = RockPaperScissorsPlayer.from_player(self.players[1])

    def determine_winner(self):
        if self.player1.choice == 1 and self.player2.choice == 1:
            return None
        if self.player1.choice == 1 and self.player2.choice == 2:
            self.player2.score += 1
            return self.player2
        if self.player1.choice == 1 and self.player2.choice == 3:
            self.player1.score += 1
            return self.player1
        if self.player1.choice == 2 and self.player2.choice == 1:
            self.player1.score += 1
            return self.player1
        if self.player1.choice == 2 and self.player2.choice == 2:
            return None
        if self.player1.choice == 2 and self.player2.choice == 3:
            self.player2.score += 1
            return self.player2
        if self.player1.choice == 3 and self.player2.choice == 1:
            self.player2.score += 1
            return self.player2
        if self.player1.choice == 3 and self.player2.choice == 2:
            self.player1.score += 1
            return self.player1
        if self.player1.choice == 3 and self.player2.choice == 3:
            return None