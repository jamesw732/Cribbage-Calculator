def powerset(s): # returns all subsets of size 2 or greater, slight optimization over all subsets
    pset = []
    x = len(s)
    s.sort()
    for i in range(2, 1 << x):
        subset = [s[j] for j in range(x) if (i & (1 << j))]
        subset.sort()
        pset.append(subset)
    pset.sort(key=len)
    return pset


def rightJack(hand, cut):
    for card in hand:
        if card != cut and card.rank == 11 and card.suit == cut.suit:
            # print("Right Jack")
            return 1
    return 0

# fifteen, run, and pair checks are all meant to be executed on subsets of a hand, not a hand itself

def isFifteen(subhand):
    sum = 0
    for card in subhand:
        rank = card.rank
        if card.rank > 10:
            rank = 10
        sum += rank
    return sum == 15

def isRun(subhand):
    if len(subhand) < 3:
        return False
    for i in range(1, len(subhand)):
        if subhand[i].rank != subhand[i - 1].rank + 1:
            return False
    return True

def isPair(subhand):
    return len(subhand) == 2 and subhand[0].rank == subhand[1].rank

def isFlush(hand):
    for i in range(1, len(hand)):
        if hand[i].suit != hand[i-1].suit:
            return False
    return True

class Card:
    suitMap = {
        "h": "Hearts",
        "d": "Diamonds",
        "s": "Spades",
        "c": "Clubs"
    }
    rankMap = { n: n for n in range(2, 11) }
    rankMap[1] = "Ace"
    rankMap[11] = "Jack"
    rankMap[12] = "Queen"
    rankMap[13] = "King"

    def __init__(self, rank, suit): # rank is an int
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(Card.rankMap[self.rank]) + " of " + str(Card.suitMap[self.suit])

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other):
        return self.rank > other.rank
    
    def __ge__(self, other):
        return self.rank >= other.rank

    def __ne__(self, other):
        return self.rank != other.rank or self.suit != other.suit

class Hand: # four card hand with cut
    def __init__(self, hand, cut):
        self.hand = hand
        hand.sort()
        if cut:
            self.cut(cut)

    def cut(self, c):
        self.cut = c
        self.handWithCut = self.hand.copy()
        self.handWithCut.append(self.cut)
        self.handWithCut.sort()

    def getAllSubhands(self):
        return powerset(self.handWithCut)

    def calculatePoints(self, crib=False):
        points = 0
        maxRunLength = 0
        if self.cut:
            points += rightJack(self.hand, self.cut)
        if isFlush(self.hand):
            if isFlush(self.handWithCut):
                # print("Flush with cut counted")
                points += 5
            elif crib == False:
                # print("Flush without cut counted")
                points += 4
            
        for subhand in reversed(self.getAllSubhands()):
            if maxRunLength == 0:
                if isRun(subhand):
                    # print("Run counted: ", end="")
                    # for card in subhand:
                    #     print(card, end=", ")
                    # print()
                    points += len(subhand)
                    maxRunLength = len(subhand)
            elif len(subhand) == maxRunLength:
                if isRun(subhand):
                    # print("Run counted: ", end="")
                    # for card in subhand:
                    #     print(card, end=", ")
                    # print()
                    points += maxRunLength
            if isFifteen(subhand):
                # print("15 counted: ", end="")
                # for card in subhand:
                #     print(card, end=", ")
                # print()
                points += 2
            if isPair(subhand):
                # print("Pair counted: ", end="")
                # for card in subhand:
                #     print(card, end=", ")
                # print()
                points += 2
        return points

