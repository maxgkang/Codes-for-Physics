import numpy as np
import matplotlib.pyplot as plt

N = 1000 # conducting 1000 iterables
t = np.linspace(0, 2 * np.pi, N) # one full period
A = 1 # amplitude in x
B = 1 # amplitude in y
w_x = 1 # angular frequency in x
w_y = 1 # angular frequency in y

def x_pos(t, alpha): # defining x(t) = A * cos(w_x * t - alpha)
    return A * np.cos(w_x * t - alpha)

def y_pos(t, beta): # fixed to cos to match harmonic oscillation and textbook!
    return B * np.cos(w_y * t - beta)

deltas = [120, 330, 360] # phase angles (delta = alpha - beta) in degrees
beta_deg = 30 # setting beta to 30 degrees (any other number is also plausible)

plt.figure(figsize=(15, 5))

for i, delta_deg in enumerate(deltas):
    alpha_deg = delta_deg + beta_deg # since delta = alpha - beta
    
    alpha_rad = np.radians(alpha_deg) # converting to radians for numpy
    beta_rad = np.radians(beta_deg)
    
    x_vals = [x_pos(j, alpha_rad) for j in list(t)] # list of x coordinates
    y_vals = [y_pos(j, beta_rad) for j in list(t)] # list of y coordinates
    
    plt.subplot(1, 3, i + 1)
    plt.plot(x_vals, y_vals, color='black')
    
    # Adding arrows for direction of motion
    t_arrow = np.pi / 4 # pick a specific point in time to place the arrow
    x0 = x_pos(t_arrow, alpha_rad)
    y0 = y_pos(t_arrow, beta_rad)
    
    t_next = t_arrow + 0.1
    x1 = x_pos(t_next, alpha_rad)
    y1 = y_pos(t_next, beta_rad)
    
    # if it's a straight line (delta modulo 180 is 0), use double arrows
    if delta_deg % 180 == 0:
        plt.annotate('', xy=(0.8, 0.8 * y_pos(0, beta_rad)/x_pos(0, alpha_rad)), 
                     xytext=(-0.8, -0.8 * y_pos(0, beta_rad)/x_pos(0, alpha_rad)), 
                     arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    else:
        plt.annotate('', xy=(x1, y1), xytext=(x0, y0), 
                     arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    plt.title(f"δ = {delta_deg}°")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    
    # Adding the parameters to the plot using plt.text
    text_x = 0.5
    text_y = 1.3
    spacing = 0.15
    plt.text(text_x, text_y, f'A = {A}', fontsize=9, color='black')
    plt.text(text_x, text_y - spacing, f'B = {B}', fontsize=9, color='black')
    plt.text(text_x, text_y - 2*spacing, f'w_x = {w_x}', fontsize=9, color='black')
    plt.text(text_x, text_y - 3*spacing, f'w_y = {w_y}', fontsize=9, color='black')
    plt.text(-1.4, 1.3, f'α = {alpha_deg}°', fontsize=9, color='black')
    plt.text(-1.4, 1.3 - spacing, f'β = {beta_deg}°', fontsize=9, color='black')
    plt.text(-1.4, 1.3 - 2*spacing, f'δ = {delta_deg}°', fontsize=9, color='black')

plt.suptitle("Two-dimensional harmonic oscillation motion for various phase angles", fontsize=14)
plt.tight_layout()
plt.show()
