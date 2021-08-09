import matplotlib.pyplot as plt
import numpy as np
import random

x = random.randint(5, 1000)
step = 0
values = []
steps = []

values.append(x)
steps.append(step)
step = step + 1
while not x == 1:
    if x % 2 == 0:
        x = x / 2
        values.append(x)
        steps.append(step)
        step = step + 1
    else:
        x = 3*x+1
        values.append(x)
        steps.append(step)
        step = step + 1

xpoints = np.array(steps)
ypoints = np.array(values)
plt.clf()
plt.plot(xpoints, ypoints, 'bo-')

for x,y in zip(xpoints,ypoints):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                (x,y), # these are the coordinates to position the label
                textcoords="offset points", # how to position the text
                xytext=(0,10), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center

plt.show()