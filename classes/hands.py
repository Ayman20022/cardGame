from classes.card import Card
from classes.deck import Deck 



class Hand(Deck):
    def __init__(self,label):
        self.label = label
        self.cards = []
        self.wincount = 0
    
    def get_label(self):
        return self.label
    
    def round_winner(self):
        self.wincount +=1