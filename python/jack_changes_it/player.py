class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, choice):
        pass

    def draw(self, how_many=7):
        pass


    def has_won(self):
        if len(self.hand) == 0:
            return self.name, True
        return self.name, False