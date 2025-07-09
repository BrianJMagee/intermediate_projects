from player import Player
from deck import Deck

class Jack_Change_It:
    def __init__(self):
        self.player_count = 0
        self.players = []
        self.deck = Deck()
        self.active_player_id = 0
        self.active_player = None
        self.game_direction = "left"
        self.play_area = []
        self.discard_area = []


    def start_game(self, player_names):
        for name in player_names:
            self.players.append(Player(name))   #create player
            self.active_player = self.players[self.active_player_id]    #set new player as active player
            hand = self.draw_for_player(7)  #draw 7 cards for player
            self.active_player.recieve_cards(hand)  #give the player the cards
            self.active_player_id += 1
        self.toggle_player()
        return

    def game_over(self):
        return self.active_player.has_won()
        

    def toggle_player(self):
        self.active_player_id += 1
        
        if self.active_player_id >= len(self.players):
            self.active_player_id = 0
        else:
            self.active_player = self.players[self.active_player_id]

    def play_for_player(self, choice):
        cards_to_play = self.active_player.play_card(choice)
        self.handle_card(cards_to_play)

    def draw_for_player(self, amount):
        new_cards = []
        new_cards = self.deck.draw_cards(how_many=amount)
        return new_cards

    def handle_card(self, card, new_suit=None):
            match card:
                case if card.rank == 1 and card.suit == "hearts":
                    pass
                
                case "two":
                    self.active_player.draw
                    pass
                
                case "five_hearts":
                    
                    pass

                case "eight":
                    #toggle player twice
                    self.toggle_player()
                    self.toggle_player()

                case "jack":
                    active_suit = new_suit
                    return active_suit
                case "queen":
                    if direction == "left":
                        direction = "right"
                        return direction
                    elif direction == "right":
                        direction = "left"
                    return direction
                case _:pass


    @staticmethod
    def is_valid_choice():
        pass

    @staticmethod
    def create_players(player_count, name):
        players_list = []
        for players in range(1, player_count):
            players_list.append(Player(name))
        
        return players