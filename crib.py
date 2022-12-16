import itertools
from math import factorial
from Card import *

def nCr(n, r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))

def handSum(hand):
    tot = 0
    for card in hand:
        if card.rank > 10:
            tot += 10
        else:
            tot += card.rank
    return tot

def runPoints(hand):
    hand.sort()
    highestRun = 0
    runSoFar = 1
    runMultiplier = 1
    firstRepeat = 0
    if len(hand) < 3:
        return False
    for i in range(1, len(hand)):
        if hand[i].rank == hand[i - 1].rank + 1:
            runSoFar += 1
            if runSoFar > highestRun:
                highestRun = runSoFar
        elif hand[i].rank == hand[i-1].rank:
            if firstRepeat == 0 or firstRepeat == hand[i].rank:
                runMultiplier += 1
                firstRepeat = hand[i].rank
            else:
                runMultiplier *= 2
        else:
            if runSoFar >= 3:
                return highestRun * runMultiplier
            runSoFar = 1
            runMultiplier = 1
    if highestRun < 3:
        return 0
    return highestRun * runMultiplier

def getAvgCribScore(pair, deck):
    total = 0
    for perm in itertools.combinations(deck, 3):
        # 15's
        fifteens = 0
        for i in range(1, 4):
            for c in itertools.combinations(perm, i):
                sum = handSum(list(c))

                if sum == 15 or sum + pair[0].rank == 15 or sum + pair[0].rank + pair[1].rank == 15:
                    fifteens += 1
                if sum + pair[1].rank == 15:
                    fifteens += 1
        total += 2 * fifteens
        # runs
        p = list(perm)
        p.append(pair[0])
        p.append(pair[1])
        p.sort()
        total += runPoints(p)

        # pairs
        amts = {i:0 for i in range(1, 14)}
        for card in p:
            amts[card.rank] += 1
        for a in amts:
            if amts[a] > 1:
                total += 2 * nCr(amts[a], 2)
        
        # right jack
        for card in p:
            if card.rank == 11:
                total += .2 # pretty bad but it doesn't seem worth it to be more precise
    return total/nCr(len(deck), 3)


def fastAvgCribScore(twoCards): #approximate crib score
    score = 0
    if twoCards[0].rank == twoCards[1].rank:
        score += 2
    
    for card in twoCards:
        if card.rank == 11:
            score += .25
    
    fifteenprobs = {1: 0.1152941176470726, 2: 0.11613876319759804, 3: 0.11131221719457914, 4: 0.11143288084465182, 5: 0.37269984917041576, 6: 0.13357466063347237, 7: 0.12368024132730332, 8: 0.11927601809954963, 9: 0.10974358974359116, 10: 0.10322775263951503, 11: 0.10322775263951503, 12: 0.10322775263951503, 13: 0.10322775263951503}
    score += 2*fifteenprobs[twoCards[0].rank] + 2*fifteenprobs[twoCards[1].rank]