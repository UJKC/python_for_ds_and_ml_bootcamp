import matplotlib.pyplot as mplpp
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

mplpp.xlabel('x')
mplpp.ylabel('y')
mplpp.title("Example")
mplpp.plot(x, y, 'r-')
mplpp.show()

mplpp.subplot(1, 2, 1) #1 rows 2 colums 1st plot
mplpp.plot(x, y, 'r')

mplpp.subplot(1, 2, 2)
mplpp.plot(x, y, 'b')
mplpp.show()

fig = mplpp.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #10% from the left, 10% from the bottom, 80% of canvas size, 80% of canvas height
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title("Example_3")
axes.plot(x, y)
mplpp.show()