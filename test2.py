
# animation pyplot

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


#now we write animation function:


def animate(i):
    x=np.arange(0.0,i,0.1)
    y = 1+np.sin(2*np.pi*x)

    ax1.clear()
    ax1.plot(x, y)




ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

#We run the animation, putting the animation to the figure (fig), running the 
#animation function of "animate," and then finally we have an interval of 1000, 
#which is 1000 milliseconds, or one second.
