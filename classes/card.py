class Card : 
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"suit : {self.suit} , rank : {self.rank} "
    
    def __lt__(self,other):
        ranks=[2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']
        if self.suit == other.suit:
            return ranks.index(self.rank) < ranks.index(other.rank)
        else :
            return self.suit < other.suit


card1=Card('Diamonds ♦',10)
card2=Card('Diamonds ♦','jack')
card3=Card('Hearts ♥',10)        
card4=Card('Clubs ♣',7)    