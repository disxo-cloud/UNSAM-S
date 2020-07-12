import random
from operator import add
#%%
def deck_of_cards(n):
    if n is str:
        raise TypeError("Please input an integer")
    deck = []
    for i in range(n):
        deck.append(random.randint(1,14))
    return deck
#%%
def play(m):
    sum = 0
    while (sum <= 21 and m != []):
        sum = sum + m.pop(0)
    return ("The new deck is {} and the sum is: {}".format(m,sum))
#%%
def play_many(m,j):
    res = []
    sum = 0
    i = 0
    for i in range (0,j,1):
        while (sum <= 21 and m != []):
            sum = sum + m.pop(0)
        res.append(sum)
        sum = 0
    return res
#%%
def who_won(res):
    max = res[0]
    for a in res:
        if a > max:
            max = a
    winners = []
    for i in range(len(res)):
        if max == res[i]:
            winners.append(1)
        else:
            winners.append(0)
    return winners
#%%
def experiment(deck,rep,n):
    d = deck_of_cards(deck)
    res = [0] * n
    for i in range(rep):
        winners = who_won(play_many(d,n))
        res = (list(map(add,res,winners)))
x    return res
#%%
print(experiment(21,10,10))