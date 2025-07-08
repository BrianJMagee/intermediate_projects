from card import *

class Deck:
    def __init__(self):
        self.this_deck = self.create_deck()
        self.top_card = self.this_deck[0]

    def create_deck(self):
        #1A,2,3,4,5,6,7,8,9,10,11J,12Q,13K
        clubs = [x for x in range(1, 14) if x not in [2,8,11,12]]    #creates the deck of clubs, minus the special cards
        hearts = [x for x in range(1, 14) if x not in [1,2,5,8,11,12]]
        spades = [x for x in range(1, 14) if x not in [2,8,11,12]]
        diamonds = [x for x in range(1, 14) if x not in [2,8,11,12]]
        list_of_suits = [clubs, hearts, spades, diamonds]
        suits = ["clubs", "hearts", "spades", "diamonds"]
        deck = []

        for suit_name, suit_ranks in zip(suits, list_of_suits):
            for rank in suit_ranks:
                deck.append(Card(suit=suit_name, rank=rank))

        deck = self.create_jacks(deck)
        deck = self.create_queens(deck)
        deck = self.create_twos(deck)
        deck = self.create_eights(deck)
        deck = self.create_ace_hearts(deck)

        return deck
    
    @staticmethod
    def create_jacks(deck):
        jacks = [["clubs", 11], ["hearts", 11], ["spades", 11], ["diamonds", 11]]
        for suit, rank in jacks:
            deck = deck.append(Card.Jack(suit=suit, rank=rank))
        return deck

    @staticmethod
    def create_queens():
        queens = [["clubs", 12], ["hearts", 12], ["spades", 12], ["diamonds", 12]]
        for suit, rank in queens:
            deck = deck.append(Card.Queen(suit=suit, rank=rank))
        return deck

    @staticmethod
    def create_twos():
        twos = [["clubs", 2], ["hearts", 2], ["spades", 2], ["diamonds", 2]]
        for suit, rank in twos:
            deck = deck.append(Card.Queen(suit=suit, rank=rank))
        return deck

    @staticmethod
    def create_eights():
        eights = [["clubs", 8], ["hearts", 8], ["spades", 8], ["diamonds", 8]]
        for suit, rank in eights:
            deck = deck.append(Card.Eight(suit=suit, rank=rank))
        return deck

    @staticmethod
    def create_ace_hearts():
        ace = [["hearts", 1]]
        for suit, rank in ace:
            deck = deck.append(Card.Ace_Of_Hearts(suit=suit, rank=rank))
        return deck


    def shuffle(self):
        pass

    def reset(self):
        pass

    def draw_cards(self, how_many, player_hand):
        match how_many:
            case 2: 
                for x in range(1, 3):
                    player_hand = player_hand.append(self.top_card)
                    self.remove(2)
                    return player_hand
            case 5: 
                for x in range(1, 4):
                    player_hand = player_hand.append(self.top_card)
                    self.remove(5)
                    return player_hand
            case 7:
                for x in range(1,8):
                    player_hand = player_hand.append(self.top_card)
                    self.remove(5)
                    return player_hand
            case _:
                pass

    def remove(self, how_many):
        self.this_deck.pop(0)