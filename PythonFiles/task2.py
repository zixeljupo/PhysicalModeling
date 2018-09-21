import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import numpy.random as random


sandbox = (2.0, 2.0)
number_of_turtles = 10
speed = 0.01
simulation_time = 1000

x_size = sandbox[0]/2
y_size = sandbox[1]/2

x = random.rand(number_of_turtles)*x_size*2 - x_size
y = random.rand(number_of_turtles)*y_size*2 - y_size

for time in range(simulation_time):

    plt.title(time)
    #plt.axis('off')
    plt.axis([-x_size, x_size, -y_size, y_size])
    plt.plot(x, y, 'bo')
    plt.pause(0.01)
    plt.clf()

    for t in range(number_of_turtles):

        x1, y1, x2, y2 = x[t], y[t], x[(t + 1) % number_of_turtles], y[(t + 1) % number_of_turtles]

        dir = x2 - x1, y2 - y1
        length = np.sqrt(dir[0] ** 2 + dir[1] ** 2)
        dir = dir[0]/length, dir[1]/length

        x[t] += speed * dir[0]
        y[t] += speed * dir[1]
        x = np.clip(x, a_min=-x_size, a_max=x_size)
        y = np.clip(y, a_min=-y_size, a_max=y_size)

plt.show()

