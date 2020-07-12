import random
#%%
'''
This is NanoJack a cut down version of blackjack the rules of which are:
-The player picks cards until the value is as close to 21 as possible.
-The deck has random cards from 1 to 14.
-The player with most points in its hand will win.
-This is a pure luck-based game, in which we make a few different functions:
-deck_of_cards(n) makes a random list of cards in which n is its length.
-play(m) pops out the cards and picks cards until It reaches 21
-who_won decides which player winds, in case of a tie, the players win.
'''
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
    while (sum < 22 and m != []):
        sum = sum + m.pop(0)
    return ("The new deck is {} and the sum is: {}".format(m,sum))
#%%
def play_many(m,j):
    res = []
    sum = 0
    i = 0
    for i in range (0,j,1):
        while (sum < 22 and m != []):
            sum = sum + m.pop(0)
        res.append(sum)
        sum = 0
    return res
#%%
def who_won(res):
    max = res[0]
    for a in res:
        if a >= max:
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
        for k in range (len(res)):
            res[k] = res[k]+winners[k]
    return res
#%%
print(experiment(1000,30,10))