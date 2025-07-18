from card import *

class Deck:
    def __init__(self):
        self.this_deck = self.create_deck()
        self.top_card = self.this_deck[0]

    def create_deck(self):
        #1A,2,3,4,5,6,7,8,9,10,11J,12Q,13K
        clubs = [x for x in range(1, 14)]    #creates the deck of clubs, minus the special cards
        hearts = [x for x in range(1, 14)]
        spades = [x for x in range(1, 14)]
        diamonds = [x for x in range(1, 14)]
        list_of_suits = [clubs, hearts, spades, diamonds]
        suits = ["clubs", "hearts", "spades", "diamonds"]
        deck = []

        for suit_name, suit_ranks in zip(suits, list_of_suits):
            for rank in suit_ranks:
                deck.append(Card(suit=suit_name, rank=rank))

        return deck
    

    def shuffle(self):
        pass

    def reset(self):
        pass

    def draw_cards(self, how_many):
        new_cards = []
        match how_many:
            case 2: 
                for x in range(1, 3):
                    new_cards.append(self.top_card)
                    self.remove(2)
                return new_cards
            case 5: 
                for x in range(1, 4):
                    new_cards.append(self.top_card)
                    self.remove(5)
                return new_cards
            case 7:
                for x in range(1,8):
                    new_cards.append(self.top_card)
                    self.remove(5)
                return new_cards
            case _:
                pass

    def remove(self, how_many):
        popped_card = self.this_deck.pop(0)
        

        #should also add to discard pile in jack_change_it. Pop returns the removed element