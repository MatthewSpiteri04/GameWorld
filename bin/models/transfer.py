class Request:
    def  __init__(self, type, game, player):
        self.type = type
        self.game = game
        self.player = player

class Response:
    def  __init__(self, message):
        self.message = message