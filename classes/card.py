class Card : 
    suits=['Clubs ♣','Diamonds ♦','Hearts ♥','Spades ♠']
    ranks=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.suit}:{self.rank} "
    
    def __lt__(self,other):
        
        if self.suit == other.suit:
            return Card.ranks.index(self.rank) < Card.ranks.index(other.rank)
        else :
            return self.suit < other.suit


