import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = int(input("Enter number of steps:"))

fig = plt.figure()
ims = []

x = 0.0
xlist = [x]

for i in range(n):
    x += (random.random() - 0.5) * 2
    xlist.append(x)
    im = plt.plot(xlist, marker='+', color = 'r')
    ims.append(im)

ani = animation.ArtistAnimation(fig,ims,interval=100)
#ani.save('rw01anim.gif', writer='imagemagick')
plt.show()