import random

def deck_of_cards(n):
    if n is str:
        raise TypeError("Please input an integer")
    deck = []
    for i in range(n):
        deck.append(random.randint(1,14))
    return deck





#%%
n=int(input("Insert a number: "))
print(deck_of_cards(n))
#%%