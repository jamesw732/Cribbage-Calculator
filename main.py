from Card import Card, Hand
from Calc import getOptimalPass, makeDeck
import random

if __name__ == "__main__":
    ''' To calculate the best pass and stats for the final hand, edit/run the following: '''
    hand = [Card(12, "s"), Card(3, "c"), Card(5, "h"), Card(5, "d"),Card(6, "s"), Card(6, "c")]
    deck = makeDeck(hand)
    random.shuffle(deck)
    print("Calculating optimal pass:")
    getOptimalPass(deck, hand, False)
    
    ''' To calculate the points of a single four card hand, edit/run the following: '''
    h = [Card(10, "s"), Card(5, "h"), Card(5, "s"), Card(5, "c")]
    cut = Card(11, "s")
    hand = Hand(h, cut)
    print("Calculating points for four-card hand:")
    print(hand.calculatePoints())
