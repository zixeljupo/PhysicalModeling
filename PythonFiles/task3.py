import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import numpy.random as random


sandbox = (80.0, 80.0)
number_of_turtles = 4
speed = 0.03
steps_count = 1000
radius = 30

x_size = sandbox[0]/2
y_size = sandbox[1]/2

angle = np.linspace(0.0, 2*np.pi, num=number_of_turtles, endpoint=False)
x = radius*np.cos(angle)
y = radius*np.sin(angle)

plt.figure(figsize=(5, 5))

dt = 10.0

for step in range(steps_count):

    time = dt*step

    plt.title(time)
    plt.axis([-x_size, x_size, -y_size, y_size])
    plt.plot(x, y, 'bo')
    plt.pause(0.001)
    plt.clf()

    done = False

    for t in range(number_of_turtles):

        x1, y1, x2, y2 = x[t], y[t], x[(t + 1) % number_of_turtles], y[(t + 1) % number_of_turtles]

        delta = (x2 - x1), (y2 - y1)
        distance = np.sqrt(delta[0] ** 2 + delta[1] ** 2)
        delta = delta[0]/distance, delta[1]/distance

        x[t] += speed * delta[0] * dt
        y[t] += speed * delta[1] * dt
        x = np.clip(x, a_min=-x_size, a_max=x_size)
        y = np.clip(y, a_min=-y_size, a_max=y_size)

        if distance < speed*dt:
            done = True

    if done:
        print(time)
        break

plt.show()
