import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import numpy.random as random


sandbox = (2.0, 2.0)
number_of_turtles = 10
max_speed = 0.01
simulation_time = 1000

x_size = sandbox[0]/2
y_size = sandbox[1]/2

x = random.rand(number_of_turtles)*x_size*2 - x_size
y = random.rand(number_of_turtles)*y_size*2 - y_size

x_speed = random.rand(number_of_turtles)*x_size*2 - x_size
x_speed = random.rand(number_of_turtles)*x_size*2 - x_size
angles = random.rand(number_of_turtles)*2*np.pi

plt.axis([-x_size, x_size, -y_size, y_size])
#plt.axis('off')

for time in range(simulation_time):

    plt.title(time)
    plt.axis([-x_size, x_size, -y_size, y_size])
    plt.plot(x, y, 'bo')
    plt.pause(0.01)
    plt.clf()

    angles += random.rand(number_of_turtles) * 0.5 - 0.25
    x += max_speed * np.cos(angles)
    y += max_speed * np.sin(angles)
    x = np.clip(x, a_min=-x_size, a_max=x_size)
    y = np.clip(y, a_min=-y_size, a_max=y_size)

plt.show()

