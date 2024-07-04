import uuid

class Player:
    def __init__(self, name):
        self.name : str = name
        self.id = str(uuid.uuid4())
