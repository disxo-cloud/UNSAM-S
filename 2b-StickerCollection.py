import random
import numpy as numpy
#%%
'''
2a - Complex Sticker Collection with packs.(See: 2a)
-le is the album, cards is the ammount of cards p/pack
-how_many_packs,  simulates filling the album once
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
#If the album has [0,0,0] it will be filled by [0,1,2]#
print(make_pack(10,3))
#%%
def how_many_packs(le,cards):
    counter = 0
    album = make_album(le)
    print(album)
    while is_there(album,0) is True:
        random_deck = make_pack(le,cards)
        for i in range(len(random_deck)):
            album[random_deck[i]] += 1
        random_deck = []
        counter += 1
    return counter, album

print(how_many_packs(670,5))
#%%