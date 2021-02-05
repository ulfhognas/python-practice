import numpy as np
import pandas as pd
from collections import Counter

deck = pd.DataFrame(index=range(36))
deck['rank'] = np.tile(np.arange(6,15,1),4)
deck['suit'] = np.repeat(np.arange(1,5,1),9)
# print(deck)

def shuffle(set, n):
    choice = np.random.choice(36, n, replace = False)
    X = set.loc[choice]
    return X

def checkEqual(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

# print(deck[['rank']])

# we will check every five-card combination
# input is a card DataFrame with 5 rows
def flushCheck(fiverows):
    flush = checkEqual(fiverows['suit'])
    return flush

def straightCheck(fiverows):
    rankset = set(fiverows['rank'])
    if (len(rankset)==5 and (max(rankset)-min(rankset))==4):
        str8=True
    elif rankset==set([14, 6, 7, 8, 9]):
        str8=True
    else:
        str8 = False
    return str8

def fourkindCheck(fiverows):
    fourkind = Counter(fiverows['rank']).most_common(1)[0][1]==4
    return fourkind

def fullhouseCheck(fiverows):
    house = Counter(fiverows['rank']).most_common(2)[0][1]==3 and Counter(
        fiverows['rank']).most_common(2)[1][1]==2
    return house

def tripsCheck(fiverows):
    trips = Counter(fiverows['rank']).most_common(2)[0][1]==3 and Counter(
        fiverows['rank']).most_common(2)[1][1]==1
    return trips

def twopairCheck(fiverows):
    twopair = Counter(fiverows['rank']).most_common(2)[0][1]==2 and Counter(
        fiverows['rank']).most_common(2)[1][1]==2
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
        if len(set(board['rank']))==4:
            successP += 1
        if len(set(board['rank']))==3:
            if tripsCheck(board)==True:
                successTR += 1
            elif twopairCheck(board)==True:
                successTP += 1
        if len(set(board['rank']))==2:
            if fourkindCheck(board)==True:
                success4 += 1
            elif fullhouseCheck(board)==True:
                successH += 1
        if len(set(board['rank']))==5:
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
