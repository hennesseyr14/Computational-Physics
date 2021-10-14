# Exercise 8.10: Cometary Orbits, b)
# Ryan Hennessey

from math import sqrt
from numpy import array,arange
from pylab import plot,xlim,ylim,xlabel,ylabel,title,show

# Constants
M = 1.989e30        # kg
G = 6.67408e-11     # m^3*kg^-1*s^-2

# Function to calculate ODE system simultaneously
# Note: u = [x,y,vx,vy]
def f(u,t):
    x = u[0]
    y = u[1]
    vx = u[2]
    vy = u[3]
    r = sqrt(x**2 + y**2)
    fx = vx
    fy = vy
    fvx = -G*M*x/r**3
    fvy = -G*M*y/r**3
    return array([fx,fy,fvx,fvy],float)

# Time interval, step size
a = 0.0
b = 3.5e9
h = 1.0e4

# Create lists for points
tpoints = arange(a,b,h)
xpoints = []
ypoints = []

# Initial condition
u = array([4e12,0,0,500],float)

# Fourth-order Runge-Kutta
for t in tpoints:
    xpoints.append(u[0])
    ypoints.append(u[1])
    k1 = h*f(u,t)
    k2 = h*f(u+0.5*k1,t+0.5*h)
    k3 = h*f(u+0.5*k2,t+0.5*h)
    k4 = h*f(u+k3,t+h)
    u += (k1+2*k2+2*k3+k4)/6

# Plot and show
plot(xpoints,ypoints)
xlim(-0.5e12,4.5e12)
ylim(-1.0e12,1.0e12)
xlabel("x")
ylabel("y")
title("y vs. x")
show()