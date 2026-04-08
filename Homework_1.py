import numpy as np
import matplotlib.pyplot as plt

N = 1000 # conducting 1000 iterables
x = np.linspace(-2,2, N) # I've set the range to be [-2, 2]
U_0 = 1 # Set U_0 as 1 for plotting
a = 1 # set a as 1 for plotting

def U(x): # defining the potential energy function
    return U_0 * ( 2 * ((x/a)**2) - (x/a) ** 4 ) 

y = [U(i) for i in list(x)] # using list comprehension to make a list of y coordinates
plt.plot(x, y, color='black')
plt.title("The graph of U(x)")
plt.xlabel("x")
plt.ylabel("Potential Energy U(x)")
plt.scatter([0], [U(0)], color='blue', zorder=5)
plt.annotate('Stable Equilibrium', xy=(0, U(0)), xytext=(-0.5, 0.1))
plt.scatter([-1, 1], [U(-1), U(1)], color='blue', zorder=5)
plt.annotate('Unstable Equilibrium', xy=(-1, U(-1)), xytext=(-1.5, 1.1))
plt.annotate('Unstable Equilibrium', xy=(1, U(1)), xytext=(0.5, 1.1))
plt.text(1.5, 1.3, 'U_0 = 1', fontsize=8, color='black')
plt.text(1.5, 1.25, 'a = 1', fontsize=8, color='black')
plt.xlim(-2, 2) 
plt.ylim(0,1.5)
plt.show()
# using matplotlib to plot the function

