import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import random

def update_bars(num, bars):
    a = random.randint(0,1)
    if a == 0:        
        i = random.randint(0, 16)
        dz[i] = 1
        bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=random.choice(['g']))
        return bars
    if a == 1:        
        i = random.randint(0, 16)
        dz[i] = -1
        bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=random.choice(['r']))
        return bars


fig = plt.figure()
ax = p3.Axes3D(fig)
xpos = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
ypos = [0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]
zpos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dx =   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
dy =   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
dz =   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  
# add bars
bars = []
for i in range(16):
    bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=['g']))
ax.set_title('Beta Forestal')

line_ani = animation.FuncAnimation(fig, update_bars, 20, fargs=[bars], interval=100, blit=False)
plt.show()