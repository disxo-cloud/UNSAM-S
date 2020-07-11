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
    

#%%
n=int(input("Insert the number of cards in your deck: "))

n=deck_of_cards(n)
print(n)
print(play(n))

# %%
