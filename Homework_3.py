import numpy as np
import matplotlib.pyplot as plt
N = 500 # conducting 500 iterables
beta = 1.0 # set beta as 1 for plotting
t = np.linspace(0, 10, N)
def pos(t, x0, v0): # defining the position function
    A = x0
    B = v0 + beta * x0
    return (A + B * t) * np.exp(-beta * t)
def vel(t, x0, v0): # defining the velocity function
    A = x0
    B = v0 + beta * x0
    return (B - beta * (A + B * t)) * np.exp(-beta * t)
for x0, v0 in [(2, 2), (4, 0), (0, 4)]: # plotting paths above the asymptote
    x = [pos(i, x0, v0) for i in list(t)] # using list comprehension to make a list of x coordinates
    y = [vel(i, x0, v0) for i in list(t)] # using list comprehension to make a list of y coordinates
    plt.plot(x, y, color='blue')
    plt.scatter([x0], [v0], color='blue', s=20)
for x0, v0 in [(-2, -2), (-4, 0), (0, -4)]: # plotting paths below the asymptote
    x = [pos(i, x0, v0) for i in list(t)]
    y = [vel(i, x0, v0) for i in list(t)]
    plt.plot(x, y, color='red')
    plt.scatter([x0], [v0], color='red', s=20)
# plotting the asymptotic line
x_line = np.linspace(-5, 5, N)
y_line = [-beta * i for i in list(x_line)]
plt.plot(x_line, y_line, 'k--')
plt.title("Phase Space Diagram for Critical Damping")
plt.xlabel("Position x")
plt.ylabel("Velocity v")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.text(3, 4, 'beta = 1', fontsize=8, color='black')
plt.grid(True)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()