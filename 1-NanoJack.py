import random
#%%

def deck_of_cards(n):
    deck = []
    for i in range(n):
        deck.append(random.randint(1,14))
    return deck


print(deck_of_cards(10))
print("Hello")
# %%
