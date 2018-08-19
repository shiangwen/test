import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
xdata, ydata = [], []
line, = plt.plot([], [], 'ro', animated=True)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    xdata=[math.cos(i*1/36*2*math.pi) for i in range(frame+1)]
    ydata=[math.sin(j*1/36*2*math.pi) for j in range(frame+1)]
    line.set_data(xdata, ydata)
    return line,

ani = FuncAnimation(fig, update, frames=36,
                    init_func=init, blit=True)
ax.set_aspect(1./ax.get_data_ratio())
plt.show()
from IPython.display import HTML
HTML(ani.to_jshtml())