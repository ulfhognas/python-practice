import numpy as np
from collections import Counter

#attempting handrankings without pandas

ranks = np.tile(np.arange(6,15,1),4)
suits = np.repeat(np.arange(1,5,1),9)
deck = np.column_stack((ranks, suits))
#print(deck)

print(deck[[10, 19],:])

def shuffle(deck, n):
    choice = np.random.choice(36, n, replace = False)
    X = deck[choice, :]
    return X

def flushCheck(hand):
    suitset = set(hand[:,1])
    flush = len(suitset)==1
    return flush

def straightCheck(hand):
    rankset = set(hand[:,0])
    if (len(rankset)==5 and (max(rankset)-min(rankset))==4):
        str8 = True
    elif rankset==set([14, 6, 7, 8, 9]):
        str8 = True
    else:
        str8 = False
    return str8

def fourkindCheck(hand):
    fourkind = Counter(hand[:,0]).most_common(1)[0][1]==4
    return fourkind

#print(fourkindCheck(deck[(0,9,18,27,28),:]))

def fullhouseCheck(hand):
    house = Counter(hand[:,0]).most_common(2)[0][1]==3 and Counter(
        hand[:,0]).most_common(2)[1][1]==2
    return house

print(fullhouseCheck(deck[(0,9,18,19,28),:]))
