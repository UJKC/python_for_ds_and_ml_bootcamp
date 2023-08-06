import matplotlib.pyplot as mplpp
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

#1
mplpp.xlabel('x')
mplpp.ylabel('y')
mplpp.title("Example")
mplpp.plot(x, y, 'r-')
mplpp.show()

#2
mplpp.subplot(1, 2, 1) #1 rows 2 colums 1st plot
mplpp.plot(x, y, 'r')
mplpp.subplot(1, 2, 2)
mplpp.plot(x, y, 'b')
mplpp.show()

#3
fig = mplpp.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #10% from the left, 10% from the bottom, 80% of canvas size, 80% of canvas height
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title("Example_3")
axes.plot(x, y)
mplpp.show()

#4
fig,axes_plt = mplpp.subplots(nrows= 1, ncols= 2)
axes_plt[0].plot(x, y, 'r')
axes_plt[1].plot(x, y, 'b')
mplpp.tight_layout()
mplpp.show()

#5
fig,axes_plt = mplpp.subplots(nrows= 2, ncols= 1, figsize= (8, 2))
axes_plt[0].plot(x, y, 'r')
axes_plt[1].plot(x, y, 'b')
mplpp.tight_layout()
mplpp.show()

#6
fig = mplpp.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #10% from the left, 10% from the bottom, 80% of canvas size, 80% of canvas height
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title("Example_3")
axes.plot(x, y, label="x, y")
axes.plot(y, x, label="y, x")
axes.legend(loc = 0)
mplpp.show()

#7
fig = mplpp.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #10% from the left, 10% from the bottom, 80% of canvas size, 80% of canvas height
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title("Example_3")
axes.plot(x, y, label="x, y", linewidth= 2, linestyle="--", marker='o', markersize='10', markeredgewidth=3)
axes.plot(y, x, label="y, x", linewidth= 3, alpha= 0.5, linestyle="steps", marker='1', markerfacecolor="yellow", markeredgecolor='green')
axes.legend(loc = 0)
mplpp.show()

#8
fig, ax = mplpp.subplots(figsize=(12,6))

ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')

# custom dash
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')

# marker size and color
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green")
mplpp.show()

#9
fig = mplpp.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #10% from the left, 10% from the bottom, 80% of canvas size, 80% of canvas height
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title("Example_3")
axes.set_xlim([0, 1])
axes.set_ylim([0, 3])
axes.plot(x, y, label="x, y", linewidth= 2, linestyle="--", marker='o', markersize='10', markeredgewidth=3)
axes.plot(y, x, label="y, x", linewidth= 3, alpha= 0.5, linestyle="steps", marker='1', markerfacecolor="yellow", markeredgecolor='green')
axes.legend(loc = 0)
mplpp.show()