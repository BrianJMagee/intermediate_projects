from jack_change_it import Jack_Change_It

class Change_It_App:
    def __init__(self, game, input = input, output = print):
        self.my_game = Jack_Change_It()
        self.play = True
    
    def play(self):
        while self.play:
            #prints output

            #gets input from active player

            #handles that input
            
            #checks if game is over
            active_player, self.play = self.my_game.game_over()

            if self.play == False:
                self.output(f"{active_player} has won!!")

            

    def output():
        pass

    def get_input():
        pass

    def handle_input():
        pass