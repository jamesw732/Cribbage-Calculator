# Cribbage-Calculator
## Overview
Calculates the points of a hand in the card game Cribbage, and provides statistics such as highest possible points for a hand, average points for a hand, etc. Also provides some information on crib points, however this analysis is heavily limited since I assume a normal distribution of cards entering the crib by the opponent (qualitatively, we'd expect that an opponent is less likely to throw a 5 to the crib than a king if they aren't the dealer, however this program does not capture this at all). Computing the same statistics with a non-normal distribution of cards would be reasonable as long as I had significant data on crib passes, however I am uncertain if this exists, and collecting it myself would require an unreasonable amount of cribbage games, and not to mention the data would vary based on opponent's skill.

## Using
This program has not been made to be very user friendly, instead the development focus was on functionality. A sample main file has been provided, simply replace the Card object parameters to what is desired. The first parameter represents rank (1-12 where 1 is Ace and 11-12 is Jack-King), and the second parameter represents suit (h = hearts, d = diamonds, h = hearts, c = clubs).
