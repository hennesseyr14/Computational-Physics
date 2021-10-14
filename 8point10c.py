# Exercise 8.10: Cometary Orbits, c)
# Ryan Hennessey

from math import sqrt
from numpy import array
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

# Function to perform fourth-order Runge-Kutta
def RK(h,u,t):
    k1 = h*f(u,t)
    k2 = h*f(u+0.5*k1,t+0.5*h)
    k3 = h*f(u+0.5*k2,t+0.5*h)
    k4 = h*f(u+k3,t+h)
    newu = u + (k1+2*k2+2*k3+k4)/6
    return newu

# Time interval
a = 0.0             # s
b = 3.5e9           # s

# Initial step size
h = 1.0e4

# Accuracy
delta = 1000/(b/2)        # 1 km per year of comet in m/s

# Create lists for points
tpoints = []
xpoints = []
ypoints = []

# Initial condition
u = array([4e12,0,0,500],float)

tpoints.append(a)
xpoints.append(u[0])
ypoints.append(u[1])

t = a

while t < b:

    # Perform two steps of size h
    u0 = RK(h,u,t)

    u1 = RK(h,u0,t+h)
    x1 = u1[0]
    y1 = u1[1]

    # Perform one step of size 2h
    u2 = RK(2*h,u,t)
    x2 = u2[0]
    y2 = u2[1]

    # Errors in x and y
    epsx = 1/30*(x2 - x1)
    epsy = 1/30*(y2 - y1)

    # Euclidean error
    error = sqrt(epsx**2 + epsy**2)

    # Ratio of target accuracy and actual accuracy
    rho = h*delta/abs(error)

    # Only append points and move on if accuracy is within desired range
    if rho > 1:
        tpoints.append(t+h)
        xpoints.append(x1)
        ypoints.append(y1)
        t += h
        u = u0

    # Modify step size
    hprime = h*rho**(1/4)

    if hprime > 2*h:
        hprime = 2*h

    h = hprime

# Plot and show
plot(xpoints,ypoints)
xlim(-0.5e12,4.5e12)
ylim(-1.0e12,1.0e12)
xlabel("x")
ylabel("y")
title("y vs. x")
show()

from numpy import absolute
r = array([49.0,-36.0,-16.0],float)
s = abs(r)
print(s)