from player import Player
from deck import Deck

class Jack_Change_It:
    def __init__(self):
        self.player_count = 0
        self.players = []
        self.deck = Deck()
        self.player_id = None
        self.active_player = None
        self.game_direction = "left"
        self.play_area = None
        self.discard_area = []


    def start_game(self, player_names):
        for name in player_names:
            self.players.append(Player(name, self.deck))
            self.players[self.player_count].draw()
            self.player_count += 1
        self.player_id = 0
        self.active_player = self.players[self.player_id]

    def game_over(self):
        return self.active_player.has_won()
        

    def toggle_player(self):
        self.player_id += 1
        self.active_player = self.players[self.player_id]

    def handle_card(self, card, new_suit=None):
            match card:
                case "ace_hearts":
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