import numpy as np
import matplotlib.pyplot as plt

N = 1000 # conducting 1000 iterables
U_0 = 1 # Set U_0 as 1 for plotting
a = 1 # set a as 1 for plotting
m = 1.0 # set m as 1 kg for plotting
t = np.linspace(0, 5, N)
w = np.sqrt(2 * U_0 / m) / a

def x(t):
    return a * np.tanh((t/a) * np.sqrt(2 * U_0 / m))

set_x = [x(i) for i in list(t)] # using list comprehension to make a list of y coordinates

plt.plot(t, set_x, color="black")
plt.title("time - position graph")
plt.xlabel("time")
plt.ylabel("x(t)")
plt.text(1.2, 0.7, 'U_0 = 1', fontsize=8, color='black')
plt.text(1.2, 0.65, 'a = 1', fontsize=8, color='black')
plt.grid(True)
plt.show()