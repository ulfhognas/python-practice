import numpy as np
from collections import Counter

#attempting handrankings without pandas

ranks = np.tile(np.arange(6,15,1),4)
suits = np.repeat(np.arange(1,5,1),9)
deck = np.column_stack((ranks, suits))

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

def tripsCheck(hand):
    trips = Counter(hand[:,0]).most_common(2)[0][1]==3 and Counter(
        hand[:,0]).most_common(2)[1][1]==1
    return trips

def twopairCheck(hand):
    twopair = Counter(hand[:,0]).most_common(2)[0][1]==2 and Counter(
        hand[:,0]).most_common(2)[1][1]==2
    return twopair

def handrankings(n):
    successF = 0
    successS = 0
    successSF = 0
    success4 = 0
    successH = 0
    successTR = 0
    successTP = 0
    successP = 0
    successHC = 0
    for i in np.arange(0,n):
        board = shuffle(deck, 5)
        if len(set(board[:,0]))==4:
            successP += 1
        if len(set(board[:,0]))==3:
            if tripsCheck(board)==True:
                successTR += 1
            elif twopairCheck(board)==True:
                successTP += 1
        if len(set(board[:,0]))==2:
            if fourkindCheck(board)==True:
                success4 += 1
            elif fullhouseCheck(board)==True:
                successH += 1
        if len(set(board[:,0]))==5:
            if flushCheck(board)==True and straightCheck(board)==True:
                successSF += 1
            elif straightCheck(board)==True:
                successS += 1
            elif flushCheck(board)==True:
                successF += 1
            else:
                successHC += 1
    rateF = successF/n
    rateS = successS/n
    rateSF = successSF/n
    rate4 = success4/n
    rateH = successH/n
    rateTR = successTR/n
    rateTP = successTP/n
    rateP = successP/n
    rateHC = successHC/n
    sum = success4 + successF + successH + successP + successS + successHC \
     + successTR + successSF + successTP
    rate = rateSF, rate4, rateF, rateH, rateS, rateTR, rateTP, rateP, rateHC, \
     sum
    return rate

print("straight flush, quads, four-of-a-kind, flush, full house, straight, trips, two pair, pair, nothing")
print(handrankings(50000))
