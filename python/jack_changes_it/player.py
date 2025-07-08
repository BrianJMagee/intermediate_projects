from deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Deck.draw_cards(7)
        self.card_count = 7

    def play_card(self, choice):
        pass

    def draw_card():
        pass

    def has_won(self):
        if self.card_count == 0:
            return self.name, True
        return