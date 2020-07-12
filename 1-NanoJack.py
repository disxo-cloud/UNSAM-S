import random

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
    return res,winners
#%%
def experiment(deck,rep,n):
    winners = []
    d = deck_of_cards(deck)
    for i in range(rep):
        winners = who_won(play_many(d,n))
    return d

#%%
n=int(input("Insert the number of cards in your deck: "))

n=deck_of_cards(n)
print(n)
print(play(n))
print(who_won(play_many(n,10)))
print(experiment(21,10,3))