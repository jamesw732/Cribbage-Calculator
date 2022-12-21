from Card import *
from crib import getAvgCribScore

suits = ["h", "d", "s", "c"]
ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def makeDeck(hand):
    return [Card(r, s) for r in ranks for s in suits if Card(r, s) not in hand]

def printStats(hand, handScore, bestCuts, passed, cribScore):
    print(f"{round(handScore, 3)} points")
    print("Hand:")
    for card in hand:
        print(card, end=", ")
    print()
    print("Cards Passed:")
    for card in passed:
        print(card, end=", ")
    print()
    print("Best Cuts: ")
    for card in bestCuts:
        print(card, end=", ")
    print()
    print("Average Crib Score:")
    print(round(cribScore, 3))

def getOptimalPass(deck, prepass, dealer):
    maxScore = 0
    minScore = 0
    maxAvg = 0
    defScore = 0
    bestDifferential = -29
    bestSum = 0
    bestSumHandPts = 0
    bestDifferentialHand = 0

    highestMax = []
    highestMin = []
    highestAvg = []
    highestDef = []
    safest = []
    sumHand = []

    optimalMaxCuts = []
    optimalMinCuts = []
    optimalAvgCuts = []
    optimalDefCuts = []
    optimalSafeCuts = []

    maxCrib = 0
    minCrib = 0
    avgCrib = 0
    defCrib = 29
    safeCrib = 0
    sumCrib = 0

    maxPass = []
    minPass = []
    avgPass = []
    defPass = []
    safePass = []
    sumPass = []

    for i in range(5):
        for j in range(i+1, 6):
            keeps = [prepass[k] for k in range(6) if k != i and k != j]
            handMax = 0
            handMin = 29
            handAvg = 0
            bestCuts = []
            for cut in deck:
                hand = Hand(keeps, cut)
                score = hand.calculatePoints()
                # local extremes for a set of four
                if score > handMax:
                    handMax = score
                    bestCuts = [cut]
                elif score == handMax:
                    bestCuts.append(cut)
                if score < handMin:
                    handMin = score
                handAvg += score
            # overall extremes
            handAvg /= 46
            cribScore = getAvgCribScore([prepass[i], prepass[j]], deck)
            if cribScore < defCrib: # update defensive pass
                highestDef = keeps
                defCrib = cribScore
                defScore = handAvg
                optimalDefCuts = bestCuts
                defPass = [prepass[i], prepass[j]]
            if handAvg > maxAvg: # update best average hand
                maxAvg = handAvg
                highestAvg = keeps
                optimalAvgCuts = bestCuts
                avgPass = [prepass[i], prepass[j]]
                avgCrib = cribScore
            if handMax > maxScore: # update best max hand
                maxScore = handMax
                highestMax = keeps
                optimalMaxCuts = bestCuts
                maxPass = [prepass[i], prepass[j]]
                maxCrib = cribScore
            if handMin > minScore: # update best min hand
                minScore = handMin
                highestMin = keeps
                optimalMinCuts = bestCuts
                minPass = [prepass[i], prepass[j]]
                minCrib = cribScore
            if (handAvg - cribScore > bestDifferential): # update safest hand
                bestDifferential = handAvg - cribScore
                safest = keeps
                safePass = [prepass[i], prepass[j]]
                bestDifferentialHand = handAvg
                optimalSafeCuts = bestCuts
                safeCrib = cribScore
            if (handAvg + cribScore > bestSum): # update best dealer hand
                bestSum = handAvg + cribScore
                sumHand = keeps
                sumPass = [prepass[i], prepass[j]]
                bestSumHandPts = handAvg
                sumCrib = cribScore
            # difference between hand avg and crib avg
    print("=================================================================================")
    print("Original Hand:")
    for card in prepass:
        print(card, end=", ")
    print("\n\n")
  
    print("Maximum Possible Score:")
    printStats(highestMax, maxScore, optimalMaxCuts, maxPass, maxCrib)


    print("\n\nHighest Minimum Score:")
    printStats(highestMin, minScore, optimalMinCuts, minPass, minCrib)

    print("\n\nHighest Average Score:")
    printStats(highestAvg, maxAvg, optimalAvgCuts, avgPass, avgCrib)

    if dealer:
        print("\n\nBest sum of crib and hand for dealer")
        for card in sumHand:
            print(card, end=", ")
        print()
        print("Pass:")
        for card in sumPass:
            print(card, end=", ")
        print()
        print("Average Hand Score:")
        print(round(bestSumHandPts, 3))
        print("Average Crib Score:")
        print(round(sumCrib, 3))
        print("Sum of hand and crib:")
        print(round(bestSum, 3))

    else:
        print("\n\nBest Defensive Pass:")
        printStats(highestDef, defScore, optimalDefCuts, defPass, defCrib)

        print("\n\nSafest Pass (best difference between avg hand and avg crib) when not dealer")
        printStats(safest, bestDifferentialHand, optimalSafeCuts, safePass, safeCrib)
        print("Average difference between hand and crib:")
        print(round(safest - safeCrib, 3))
