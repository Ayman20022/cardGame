from card import Card
import random as rd


class Deck:
    cards=[]
    def __init__(self) -> None:
        for suit in Card.suits:
            for rank in Card.ranks:
                Deck.cards.append(Card(suit=suit,rank=rank))
    
    def __str__(self):
        str_cards=''
        for card in Deck.cards:
            str_cards+='['
            str_cards+=str(card)
            str_cards+='],'
        return str_cards
    
    def add_card(card):
        Deck.cards.append(card)
    def shuffle(self):
        rd.shuffle(Deck.cards)
    def pop_card(self):
        return Deck.cards.pop(-1)

        