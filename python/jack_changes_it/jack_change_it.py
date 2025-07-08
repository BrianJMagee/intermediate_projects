from player import Player
from deck import Deck

class Jack_Change_It:
    def __init__(self, player_count):
        self.players = self.create_players(player_count=player_count, name="Brian")
        self.deck = Deck()
        self.player_id = 0
        self.active_player = self.players[self.player_id]
        self.game_direction = "left"
        self.play_area = None

    def game_over(self):
        return self.active_player.has_won()
        

    def toggle_player(self):
        self.player_id += 1
        self.active_player = self.players[self.player_id]

    def handle_card(self, card):
            match card:
                
                case ace_hearts:

                case two:
                    
                    pass
                
                case five_hearts:
                    
                    pass

                case eight:
                    #toggle player twice
                    pass

                case jack:
                    active_suit = new_suit
                    return active_suit
                case queen:
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