from jack_change_it import Jack_Change_It

class Change_It_App:
    def __init__(self, input = input, output = print):
        self.my_game = Jack_Change_It()
        self.loop = True
        self.menu = ["Play card", "Draw card"]
        self.input = input
        self.output = output
    
    def play(self):
        names = ["Brian", "Joseph", "Kevin", "Magee"]
        self.my_game.start_game(names)
        while self.loop:
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
        name = self.my_game.active_player.name
        self.output(f"Player: {self.my_game.active_player.name}")
        self.output(f"Your hand: ")
        for card in self.my_game.active_player.hand:
            self.output(f"{count}: {card.rank} of {card.suit}")
            count += 1

    def get_input(self):
        choice = int(self.input("Please enter a card to add to your hand to play: "))
        return choice

    def handle_input(self, choice):
        #takes the card at the index "choice" and passes it to the game
        self.my_game.handle_card(self.my_game.active_player.hand[choice])