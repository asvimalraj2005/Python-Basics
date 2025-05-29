# A deck as a sequence of playing cards
import collections                                                # Importing collections 
Card = collections.namedtuple('Card',['rank','suit'])             # By using collections we are creating a card with rank and suit 
class FrenchDeck:                                                 # Creating a class named FrenchDeck
    ranks = [str(n) for n in range(2,11)]+['F','T','S','M']       # By using for loop we are traversing on the deck J K Q A 
    suits='spades diamonds clubs hearts'.split()                  # We are splitting the spades diamons clubs hearts according to them 
    
    def __init__(self):                                           # Creating a constructor where cards with its rank and suits are being called from the list 
        self._cards=[Card(rank,suit) for suit in self.suits 
                                         for rank in self.ranks]
    
    def __len__(self):                                            # len of cards in total
        return len(self._cards)
    
    def __getitem__(self,position):                               # The cards are now shuffled and positioned 
        return self._cards[position]
    
deck=FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])                    # Output 
#                                   52
#                                   Card(rank='2', suit='spades')
#                                   Card(rank='A', suit='hearts')
#
#   


                                        