from deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = self.draw()
        self.card_count = 7

    def play_card(self, choice):
        pass

    def draw(self, how_many=7):
        hand = []
        hand = Deck.draw_cards(how_many=how_many, player_hand=hand)
        self.hand = hand

    def get_hand(self):
        return self.hand


    def has_won(self):
        if self.card_count == 0:
            return self.name, True
        return