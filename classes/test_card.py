from card import Card
from deck import Deck

card1=Card('Diamonds ♦','10')
card2=Card('Diamonds ♦','Jack')
card3=Card('Hearts ♥','10')        
card4=Card('Clubs ♣','7')    

print(card1<card2)
print(card4<card1)


deck = Deck()
print(deck)
print(len(deck.cards))
deck.pop_card()
deck.shuffle()
print(len(deck.cards))
print(deck)
deck.cards.sort()
print(deck)

