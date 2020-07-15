import random
import numpy as np
#%%
'''
2a - Simple Sticker Collection.(Buying without packs)
-is_there(checks if element is in album)
-buy_sticker(returns a sticker)
-fill_once, returns a counter and the filled album with repeats
-fill_many, fills a list with the counter in x times, returns
mean value of filling many albums
'''
#%%
def make_album(le):
    return [0]*le
print(make_album(10))
#%%
def is_there(l,e):
    if e in l:
        return True
    else:
        return False
print(is_there(make_album(10),1))
#%%
def buy_sticker(le):
    return random.randint(0,le-1)
print(buy_sticker(10))
#%%
def fill_once(le):
    counter = 0
    album = make_album(le)
    while is_there(album,0) is True:
        album[buy_sticker(le)] += 1
        counter += 1
    return counter, album

print("AAA")
print(fill_once(10))
#%%
def fill_many(le,times):
    counter = 0
    album = make_album(le)
    result = []
    for i in range(times):
        while is_there(album,0) is True:
            album[buy_sticker(le)] += 1
            counter += 1
        result.append(counter)
        counter = 0
        album = make_album(le)
    return ("mean of arr : ", np.mean(result)) 
print(fill_many(670,100))