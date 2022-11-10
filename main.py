from classes.card import Card
from classes.deck import Deck
from classes.hands import Hand




d=Deck()

h1=Hand('p1')
h2=Hand('p2')
h3=Hand('p3')
h4=Hand('p4')


while len(d.cards):
    h1.add_card(d.pop_card())
    h2.add_card(d.pop_card())
    h3.add_card(d.pop_card())
    h4.add_card(d.pop_card())

Players=[h1,h2,h3,h4]

for i in range(13):
    round=[h1.pop_card(),h2.pop_card(),h3.pop_card(),h4.pop_card()]
    index = round.index(max(round))
    Players[index].round_winner()

print(h1.wincount)
print(h2.wincount)
print(h3.wincount)
print(h4.wincount)

