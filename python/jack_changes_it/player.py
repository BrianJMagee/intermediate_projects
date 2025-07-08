class Player:
    def __init__(self, name, deck):
        self.name = name
        self.hand = []
        self.deck = deck

    def play_card(self, choice):
        pass

    def draw(self, how_many=7):
        self.hand = self.deck.draw_cards(how_many=how_many, player_hand=self.hand)


    def has_won(self):
        if len(self.hand) == 0:
            return self.name, True
        return self.name, False