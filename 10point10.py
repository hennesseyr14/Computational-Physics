# Exercise 10.10: Global minimum of a function
# Ryan Hennessey

# Please do not copy and paste this program.

from math import cos,pi,sqrt,log,exp
from random import random
from pylab import plot,title,xlabel,ylabel,show

Tmax = 10.0
Tmin = 1e-3
tau = 1e4
sigma = 1.0

def f(x):
    return x**2 - cos(4*pi*x)

# Function to generate Gaussian random number
def gaussian():
    r = sqrt(-2*sigma**2*log(1-random()))
    theta = 2*pi*random()
    return r*cos(theta)

# Main loop
t = 0
T = Tmax
x = 2.0
y = f(x)
tpoints = [t]
xpoints = [x]
while T>Tmin:

    t += 1
    T = Tmax*exp(-t/tau)        # Cooling

    deltax = gaussian()
    oldx = x
    oldy = y
    x += deltax
    y = f(x)
    deltay = y - oldy

    # If move is rejected, keep original x, y
    if random() > exp(-deltay/T):
        x = oldx
        y = oldy

    tpoints.append(t)
    xpoints.append(x)

plot(tpoints,tpoints)
title("x vs. t")
xlabel("x")
ylabel("t")
show()