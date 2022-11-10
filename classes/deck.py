from classes.card import Card
import random as rd


class Deck:
    def __init__(self) -> None:
        self.cards=[]
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit=suit,rank=rank))
    
    def __str__(self):
        str_cards=''
        for card in self.cards:
            str_cards+='['
            str_cards+=str(card)
            str_cards+='],'
        return str_cards
    
    def add_card(self,card):
        self.cards.append(card)
    def shuffle(self):
        rd.shuffle(self.cards)
    def pop_card(self):
        return self.cards.pop(0)

        