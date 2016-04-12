# -*- coding: utf-8 -*-
# Homework_Random
# =============================================================================
import numpy as np

#------------------------------------------------------------------------------
# Problem 1
#------------------------------------------------------------------------------
N = 100
integerList = np.random.randint(1, 3, N)
nrHeads = 0
for i in integerList:
    if i == 1:
        nrHeads += 1

print("The number of heads is: ", nrHeads)
print("----------------------------------")

#------------------------------------------------------------------------------
# Problem 2
#------------------------------------------------------------------------------
def uni(N):
    M = 0
    for i in range(N):
        if (0.5 <= np.random.rand() <= 0.6):
            M += 1

    print("Numbers of draws: ", N)
    print("Interval: (.5, .6)")
    print("Numbers in the interval: ", M)
    print("The probability of a number falling in the interval: {:2.6f}".format(M/N))
    print("--------------------------------------------------------------")
uni(100)
uni(1000)
uni(10000)
print("----------------------------------")

#------------------------------------------------------------------------------
# Problem 3
#------------------------------------------------------------------------------
N = 1000
nrSixes = 0
for i in range(N):
    if np.random.randint(1, 7) == 6:
        nrSixes += 1
print("The number of sixes is: ", nrSixes)
print("----------------------------------")

#------------------------------------------------------------------------------
# Problem 4
#------------------------------------------------------------------------------
N = 1000
def myGame(N):
    dice1 = np.random.randint(1, 7, N)
    dice2 = np.random.randint(1, 7, N)
    dice3 = np.random.randint(1, 7, N)
    dice4 = np.random.randint(1, 7, N)
    diceSum = dice1 + dice2 + dice3 + dice4

    nWins = 0
    nLosses = 0
    nDollars = 0
    for i in range(N):
        if diceSum[i] < 9:
            nWins += 1
            # Here I count the net wins: $10-$1 = $9
            nDollars += 9
        else:
            nLosses += 1
            nDollars -= 1
    if nDollars < 0:
        print("You should not play this game")
    else:
        print("You should play this game")
    print('---------------------------------')
    print("The number of wins is: ", nWins)
    print("The number of losses is: ", nLosses)
    print("The amount won is: ", nDollars)
    print('---------------------------------')

# Now we play
myGame(1000)
