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

print(generate_forest(4))
#%%

def spawn_trees(num, bars):
    countTrees = dz.count(1)
    while ((countTrees) < len(dz)*(80/100)):#Fills until desired %#
        i = random.randint(0, len(dx))
        if dz[i] == 0.5:
            return bars
        else:
            dz[i] = 1
            bars[i].remove()
            bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=['g'])
            countTrees += 1
            return bars
    return bars

#%%


#Propagate Fire#
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


def propagate_fire(num,bars):
    i = random.randint(0,len(dx))
    while dz.count(0.5) != 1:
        if dz[i + 1] == 1:
            bars[i + 1].remove()
            bars[i + 1] = ax.bar3d(xpos[i+1], ypos[i+1], zpos[i+1], dx[i+1], dy[i+1], 0.4, color=['r'])
        elif dz[i - 1] == 1:
            bars[i - 1].remove()
            bars[i - 1] = ax.bar3d(xpos[i-1], ypos[i-1], zpos[i-1], dx[i-1], dy[i-1], 0.4, color=['r'])
        elif dz[i+n] == 1:
            bars[i+n].remove()
            bars[i + n] = ax.bar3d(xpos[i+n], ypos[i+n], zpos[i+n], dx[i+n], dy[i+n], 0.4, color=['r'])
        else:
            bars[i-n].remove()
            bars[i - n] = ax.bar3d(xpos[i-n], ypos[i-n], zpos[i-n], dx[i-n], dy[i-n], 0.4, color=['r'])
    return bars
'''
def extinguish_fire(num,bars):
    while dz.count(0.5) != 0:
        i = random.randint(0,len(dx))
        if dz[i] == 0.5: 
            dz[i] = 0
            bars[i].remove()
            bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=['k'])
            return bars
    return bars
'''

#%%
f = 0
def updateall(num,bars):
    a = spawn_trees(num,bars)
    c = spawn_thunder(num,bars)
    d = propagate_fire(num,bars)
    '''
    aa = extinguish_fire(num,bars)
    '''
    global f
    f += 1
    ax.set_title('Pasos de tabla: {}'.format(f))
    return a + c + d

#%%

n = int(input("Please Input the length of the forest grid: "))

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


for i in range(10):
    i = random.randint(0, len(dx))
    dz[i] = 1
    bars[i].remove()
    bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=['g'])


line_ani = animation.FuncAnimation(fig, updateall, 10, fargs=[bars], interval=1, blit=False)
plt.show()

#%%



