import random
import numpy as np
import matplotlib.pyplot as plt
#%%
'''
2a - Complex Sticker Collection with packs.(See: 2a)
-le is the album, cards is the ammount of cards p/pack
'''
def make_album(le):
    return [0]*le
#%%
def is_there(l,e):
    if e in l:
        return True
    else:
        return False
#%%
def make_pack(le,cards):
    pack = []
    for i in range(cards):
        pack.append(random.randint(0,le-1))
    return pack
#I take 0 as one of the possible values#
#If the album is [0,0,0] it will be filled by [0,1,2]#
#%%
def how_many_packs(le,cards):
    counter = 0
    album = make_album(le)
    while is_there(album,0) is True:
        random_deck = make_pack(le,cards)
        for i in range(len(random_deck)):
            album[random_deck[i]] += 1
        random_deck = []
        counter += 1
    return counter

#%%
def mean_how_many_packs(n,le,cards):
    mean = []
    for k in range(n):
        counter = 0
        album = make_album(le)
        while is_there(album,0) is True:
            random_deck = make_pack(le,cards)
            for i in range(len(random_deck)):
                album[random_deck[i]] += 1
            random_deck = []
            counter += 1
        mean.append(counter)
    return np.mean(mean)
#%%
#We will now plot the probabilities of filling the album#
def percentage_pack(Npacks,le,pre,cards):
    count = [0]
    per = []
    percentage = []
    counter = 0
    for i in range(pre):
        album = make_album(le)
        for k in range(Npacks):
            count = []
            random_deck = make_pack(le,cards)
            for j in range(len(random_deck)):
                album[random_deck[j]] += 1
            for l in range(len(album)):
                if album[l] != 0:
                    counter += 1
            count.append(counter)
            counter = 0
        per.append((count[0]*100)/le)
    percentage.append(np.mean(per))
    per = []
    return np.mean(percentage)

print(percentage_pack(900,682,1,5))


#%%
#This plot will determine those probabilities
#It takes time and will never tell the optimum number#
def percentages_packs(N,le,pre,cards):
    li = []
    for i in range(N):
        li.append(percentage_pack(i,le,pre,cards))
    return li
height = (percentages_packs(1000,682,1,5))
#%%
y_pos = (np.arange(len(height)))
plt.bar(y_pos,height)
plt.show()
