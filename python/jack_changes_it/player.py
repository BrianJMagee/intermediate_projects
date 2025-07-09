class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, choice):
        hand_to_play = []
        for crd in choice:
            hand_to_play.append(self.hand[crd])
            choice.pop(crd)
        return hand_to_play
        

    def recieve_cards(self, new_cards):
        for crd in new_cards:
            self.hand.append(crd)
        return


    def has_won(self):
        if len(self.hand) == 0:
            return self.name, True
        return self.name, False