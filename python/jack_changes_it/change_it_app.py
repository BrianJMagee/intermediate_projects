from jack_change_it import Jack_Change_It

class Change_It_App:
    def __init__(self, input = input, output = print):
        self.my_game = Jack_Change_It(5)
        self.play = True
        self.menu = ["Play card", "Draw card"]
    
    def play(self):
        while self.play:
            self.output("******************************************")
            self.output("Jack Change it!!")
            #prints output
            self.print_output()

            #gets input from active player
            choice = self.get_input()

            #handles that input
            self.handle_input(choice)
            
            #checks if game is over
            active_player, self.play = self.my_game.game_over()

            if self.play == False:
                self.output(f"{active_player} has won!!")
                self.output("******************************************")

            

    def print_output(self):
        count = 1

        self.output(f"Player: {self.my_game.active_player.name}")
        self.output(f"Your hand: ")
        for card in self.my_game.active_player.get_hand():
            for suit, rank in card:
                self.output(f"{count}: {rank} of {suit}")
                count += 1

    def get_input(self):
        self.my_game.active_player

    def handle_input():
        pass