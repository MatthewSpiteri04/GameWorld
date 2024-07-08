import uuid

class Player:
    def __init__(self, name):
        self.name : str = name
        self.id = str(uuid.uuid4())

class RockPaperScissorsPlayer(Player):
    def __init__(self, name, id):
        super().__init__(name)
        self.name : str = name
        self.id = id
        self.score = 0
        self.ready = False
        self.choice = 0

    @classmethod
    def from_player(cls, player : Player):
        return cls(player.name, player.id)
