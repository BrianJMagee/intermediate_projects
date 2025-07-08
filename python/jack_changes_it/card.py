class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.value = rank

class Queen(Card):
    def change_direction(direction):
        if direction == "left":
            direction = "right"
            return direction
        elif direction == "right":
            direction = "left"
            return direction

class Jack(Card):
    def change_active_suit(active_suit, new_suit):
        active_suit = new_suit
        return active_suit

class Eight(Card):
    def skip_next_player():
        #toggle player twice
        pass

class Five_Of_Hearts(Card):
    def counter_ace_hearts():
        pass

class Two(Card):
    def draw_two():
        pass

class Ace_Of_Hearts(Card):
    def draw_five():
        pass