from jack_change_it import Jack_Change_It

class Change_It_App:
    def __init__(self, input = input, output = print):
        self.my_game = Jack_Change_It()
        self.loop = True
        self.menu = ["Play card", "Draw card"]
        self.input = input
        self.output = output
    
    def play(self):
        self.output("Please enter each player's name")
        count = 1
        names = []

        while self.loop:
            name = self.input(f"Player {count} name: ")
            names.append(name)
            count+=1

            another = self.input("Add another player y/n: ")
            if another == "n":
                self.loop = False
        
        self.my_game.start_game(names)

        self.loop = True
        while self.loop:
            self.output("******************************************")
            self.output("Jack Change it!!")
            #prints output
            self.print_hand()

            #gets input from active player
            choice = self.get_input()

            #handles that input
            self.handle_input(choice)
            
            #checks if game is over
            active_player, is_over = self.my_game.game_over()

            if is_over == False:
                self.output(f"{active_player} has won!!")
                self.output("******************************************")
                break

            

    def print_hand(self):
        count = 1
        self.output(f"Player: {self.my_game.active_player.name}")
        self.output(f"Your hand: ")
        for card in self.my_game.active_player.hand:
            self.output(f"{count}: {card.rank} of {card.suit}")
            count += 1

    def get_input(self):
        choice = int(self.input("Please enter the cards you want to play: "))
        return choice

    def handle_input(self, choice, new_suit=None):
        #takes the card at the index "choice" and passes it to the game
        self.my_game.handle_card(choice, new_suit=new_suit)