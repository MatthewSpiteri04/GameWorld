class Request:
    def  __init__(self, type, game, data, player_num = None):
        self.type = type
        self.game = game
        self.data = data
        self.player_num = player_num

class Response:
    def  __init__(self, message, data):
        self.message = message
        self.data = data