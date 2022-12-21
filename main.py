from Card import Card
from Calc import getOptimalPass, makeDeck
import random

if __name__ == "__main__":
    hand = [Card(12, "s"), Card(3, "c"), Card(5, "h"), Card(5, "d"),Card(6, "s"), Card(6, "c")]
    deck = makeDeck(hand)
    random.shuffle(deck)
    
    getOptimalPass(deck, hand, False)