import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np
import random

def gen_bosque(n):
    arr = []
    for i in range(n):
        arr.append(i)
    xpos = np.repeat(arr, n)
    ypos = arr * n 
    zpos = [0] * (n * 4)
    dx = [1] * (n * 4)
    dy = [1] * (n * 4)
    dz = [0] * (n * 4)
    return xpos,ypos,zpos,dx,dy,dz

#%%
def update_bars(num, bars):
    a = random.randint(0,1)
    if a == 0:        
        i = random.randint(0, 16)
        dz[i] += 1
        bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=random.choice(['g']))
        return bars
    if a == 1:        
        i = random.randint(0, 16)
        dz[i] = -1
        bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=random.choice(['r']))
        return bars

def update_bars0(num, bars):
    a = random.randint(0,1)
    if a == 0:        
        i = random.randint(0, 16)
        dz[i] += 5
        bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=random.choice(['g']))
        return bars
    if a == 1:        
        i = random.randint(0, 16)
        dz[i] = -1
        bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=random.choice(['r']))
        return bars

def updateall(num,bars):
    a = update_bars(num,bars)
    b = update_bars0(num,bars)
    return a + b

#%%

n = int(input("Please Input the length of the forest grid: "))

fig = plt.figure()
ax = p3.Axes3D(fig)


xpos = (gen_bosque(n))[0]
ypos = (gen_bosque(n))[1]
zpos = (gen_bosque(n))[2]
dx = (gen_bosque(n))[3]
dy = (gen_bosque(n))[4]
dz = (gen_bosque(n))[5]




# add bars
bars = []
for i in range(16):
    bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=['g']))
ax.set_title('Beta Forestal')

line_ani = animation.FuncAnimation(fig, updateall, 20, fargs=[bars], interval=100, blit=False)
plt.show()