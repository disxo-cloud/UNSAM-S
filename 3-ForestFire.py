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

def update_bars(num, bars):
    a = random.randint(0,1)
    if a == 0:        
        i = random.randint(0, len(dx))
        dz[i] += 1
        bars[i].remove()
        bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=random.choice(['g']))
        return bars
    if a == 1:        
        i = random.randint(0, len(dx))
        dz[i] = 0
        bars[i].remove()
        bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=random.choice(['b']))
        return bars

def updateall(num,bars):
    a = update_bars(num,bars)
    return a

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
    bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=['g']))
ax.set_title('Beta Forestal')

line_ani = animation.FuncAnimation(fig, updateall, 10, fargs=[bars], interval=1, blit=False)
plt.show()

#%%



