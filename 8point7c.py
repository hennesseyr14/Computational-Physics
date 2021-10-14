# Exercise 8.7: Trajectory with air resistance, c)
# Ryan Hennessey

from math import pi,sqrt,sin,cos
from numpy import array,arange
from pylab import plot,ylim,xlabel,ylabel,title,show

# Constants
m = 1               # kg
R = .08             # m
theta = 30*pi/180   # radians
v = 100             # m*s^-1
rho = 1.22          # kg*m^-3
C = 0.47
g = 9.81            # m*s^-2

# Function to calculate ODE system simultaneously
# Note: r = [x,y,xdot,ydot]
def f(r,t):
    xdot = r[2]
    ydot = r[3]
    fx = xdot
    fy = ydot
    fxdot = -(pi*R**2*rho*C)/(2*m)*xdot*sqrt(xdot**2 + ydot**2)
    fydot = -g - (pi*R**2*rho*C)/(2*m)*ydot*sqrt(xdot**2 + ydot**2)
    return array([fx,fy,fxdot,fydot],float)

# Interval, number of points, step size
a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

# Create lists for points
tpoints = arange(a,b,h)

for m in range(1,11):
    # Create lists for points
    xpoints = []
    ypoints = []
    xdotpoints = []
    ydotpoints = []

    # Fourth-order Runge-Kutta
    r = array([0.0,0.0,v*cos(theta),v*sin(theta)],float)
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        xdotpoints.append(r[2])
        ydotpoints.append(r[3])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6

    # Plot
    plot(xpoints,ypoints)

# Show graphs for comparison
ylim(0,120)
xlabel("x")
ylabel("y")
title("y vs. x")
show()