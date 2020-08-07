#%%
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

#%%
#Function to generate a forest#
#Forest is a 3d grid, xpos, ypos and zpos determine Position#
#dx dy and dz are always 1,1, and 0 to make 1x1 cubes#

def generate_forest(n):
    arr = []
    for i in range(n):
        arr.append(i)
    xpos = np.repeat(arr, n)
    ypos = arr * n 
    zpos = [0] * (n * n)
    dx = [1] * (n * n)
    dy = [1] * (n * n)
    dz = [0] * (n * n)
    return xpos,ypos,zpos,dx,dy,dz

#%%

#Functions that we will use to work on the empty Forest#
#River needs some work for more organic forms#

def spawn_river(num, bars):
    if dz.count(-0.5) < m:
        i = random.randint(0,len(dx))
        dz[i] = -0.5
        bars[i].remove()
        bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=['b'])
        return bars
    else:
        return bars

#%%

def spawn_trees(num, bars):
    countTrees = dz.count(1)
    while ((countTrees) < len(dz)*(j/100)):#Fills until desired %#
        i = random.randint(0, len(dx))
        if dz[i] == -0.5:
            return bars
        else:
            dz[i] = 1
            bars[i].remove()
            bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=['g'])
            countTrees += 1
            return bars
    return bars
#%%
#Spawning Thunder#
def spawn_thunder(num,bars):
    a = random.random()
    if a >= 0.7:   
        i = random.randint(0, len(dx))
        if dz[i] == -0.5:
            return bars
        if dz[i] == 0:
            return bars
        else:
            dz[i] = 0.5
            bars[i].remove()
            bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=['r'])
            return bars
    else:        
        return bars
#%%
'''
#Propagate Fire#

def propagate_fire(num,bars):
    i = random.randint(0,len(dx))
    while dz.count(0.5) != 0:
        bars[i].remove()
        bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], 0.5, color=['magenta'])
        if bars[i + 1] == 1:
            bars[i+1].remove()
            bars[i+1] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], 0.5, color=['magenta'])
        elif bars[i - 1] == 1:
            bars[i-1].remove()
            bars[i-1] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], 0.5, color=['magenta'])
        return bars
    while dz.count(0.5) != 0:
        if bars[i] == 0.5:
            bars[i].remove()
            bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], 0.5, color=['springgreen'])
    return bars

'''


#%%

def updateall(num,bars):
    a = spawn_river(num,bars)
    b = spawn_trees(num,bars)
    c = spawn_thunder(num,bars)
    '''
    d = propagate_fire(num,bars)
    '''
    return a + b + c

#%%

n = int(input("Please Input the length of the forest grid: "))
j = int(input("Input the percentage of terrain covered in trees p/turn: "))
m = int(input("Input the length of the river: "))
k = int(input("Input the chance of thunder per tile: "))


fig = plt.figure()
ax = p3.Axes3D(fig)


xpos = (generate_forest(n))[0]
ypos = (generate_forest(n))[1]
zpos = (generate_forest(n))[2]
dx = (generate_forest(n))[3]
dy = (generate_forest(n))[4]
dz = (generate_forest(n))[5]

print(dx)
print(dy)

a = n*n 

bars = []
for i in range(len(dx)):
    bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=['springgreen']))
ax.set_title('Beta Forestal')

line_ani = animation.FuncAnimation(fig, updateall, 10, fargs=[bars], interval=1, blit=False)
plt.show()

#%%



