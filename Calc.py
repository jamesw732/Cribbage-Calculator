from Card import *
from crib import getAvgCribScore
import random

suits = ["h", "d", "s", "c"]
ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# def getAvgCribScore(deck, twoCards): # inputs are two cards you pass and all possible cards that could make up crib
#     totalHands = 0
#     totalScore = 0
#     for i in range(len(deck) - 1):
#         crib1 = deck[i]
#         for j in range(i + 1, len(deck)):
#             crib2 = deck[j]
#             for cut in deck:
#                 if cut != crib1 and cut != crib2:
#                     hand = Hand([crib1, crib2, twoCards[0], twoCards[1]], cut)
#                     totalHands += 1
#                     totalScore += hand.calculatePoints(True)
#     return totalScore / totalHands




def makeDeck(hand):
    return [Card(r, s) for r in ranks for s in suits if Card(r, s) not in hand]


def getOptimalPass(deck, prepass):
    maxScore = 0
    minScore = 0
    maxAvg = 0
    bestDefPts = 29
    bestDifferential = -29
    bestSum = 0
    bestSumHandPts = 0
    bestSumCribPts = 0

    bestDifferentialCrib = 0
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
            if cribScore < bestDefPts:
                highestDef = keeps
                bestDefPts = cribScore
                defPass = [prepass[i], prepass[j]]
            if handAvg > maxAvg:
                maxAvg = handAvg
                highestAvg = keeps
                optimalAvgCuts = bestCuts
                avgPass = [prepass[i], prepass[j]]
            if handMax > maxScore:
                maxScore = handMax
                highestMax = keeps
                optimalMaxCuts = bestCuts
                maxPass = [prepass[i], prepass[j]]
            if handMin > minScore:
                minScore = handMin
                highestMin = keeps
                optimalMinCuts = bestCuts
                minPass = [prepass[i], prepass[j]]
            if (handAvg - cribScore > bestDifferential):
                bestDifferential = handAvg - cribScore
                safest = keeps
                safePass = [prepass[i], prepass[j]]
                bestDifferentialCrib = cribScore
                bestDifferentialHand = handAvg
            if (handAvg + cribScore > bestSum):
                bestSum = handAvg + cribScore
                sumHand = keeps
                sumPass = [prepass[i], prepass[j]]
                bestSumHandPts = handAvg
                bestSumCribPts = cribScore
            # difference between hand avg and crib avg
    print("=================================================================================")
    print("Original Hand:")
    for card in prepass:
        print(card, end=", ")
    print("\n")
    # print("Maximum Possible Score:")
    # print(maxScore)
    # for card in highestMax:
    #     print(card, end=", ")
    # print()
    # print("Best Cuts:")
    # for card in optimalMaxCuts:
    #     print(card, end=", ")
    # print()
    # print("Cards Passed: ")
    # for card in maxPass:
    #     print(card,end=", ")
    # print()
    # print("Average Crib Score:")
    # print(getAvgCribScore(maxPass, deck))
    # print("\n")


    # print("Highest Minimum Score:")
    # print(minScore)
    # for card in highestMin:
    #     print(card, end=", ")
    # print()
    # print("Best Cuts:")
    # for card in optimalMinCuts:
    #     print(card, end=", ")
    # print()
    # print("Cards Passed: ")
    # for card in minPass:
    #     print(card,end=", ")
    # print()
    # print("Average Crib Score:")
    # print(getAvgCribScore(minPass, deck))
    # print("\n")


    # print("Highest Average Score:")
    # print(maxAvg)
    # for card in highestAvg:
    #     print(card, end=", ")
    # print()
    # print("Best Cuts:")
    # for card in optimalAvgCuts:
    #     print(card, end=", ")
    # print()
    # print("Cards Passed: ")
    # for card in avgPass:
    #     print(card,end=", ")
    # print()
    # print("Average Crib Score:")
    # print(getAvgCribScore(avgPass, deck))
    # print("\n")

    # print("Best Defensive Pass:")
    # for card in defPass:
    #     print(card, end=", ")
    # print()
    # print("Average Crib Score:")
    # print(bestDefPts)
    # print("\n")

    print("Safest Pass (best difference between avg hand and avg crib) when not dealer")
    print("Hand:")
    for card in safest:
        print(card, end=", ")
    print()
    print("Average Hand Score:")
    print(round(bestDifferentialHand, 3))
    for card in safePass:
        print(card, end=", ")
    print()
    print("Average Crib Score:")
    print(round(bestDifferentialCrib, 3))
    
    print("Difference between hand and crib:")
    print(round(bestDifferential, 3))
    print("\n")
    
    print("Best sum of crib and hand for dealer")
    for card in sumHand:
        print(card, end=", ")
    print()
    print("Pass:")
    for card in sumPass:
        print(card, end=", ")
    print("Average Hand Score:")
    print(round(bestSumHandPts, 3))
    print("Average Crib Score:")
    print(round(bestSumCribPts, 3))
    print("Sum of hand and crib:")
    print(round(bestSum, 3))


if __name__ == "__main__":
    hand = [Card(12, "s"), Card(3, "c"), Card(5, "h"), Card(5, "d"),Card(6, "s"), Card(6, "c")]
    deck = makeDeck(hand)
    random.shuffle(deck)

    # print(prepass[0])
    # print(prepass[1])
    # print(getAvgCribScore(deck, [prepass[0], prepass[1]]))
    
    getOptimalPass(deck, hand)