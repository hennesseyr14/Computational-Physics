# 8.16  The three-body problem, b)
# Ryan Hennessey

from numpy.linalg import norm
from numpy import array,sqrt,absolute,size
from pylab import plot,show

# Constants (in arbitrary units)
m1 = 150        # Mass of Star 1
m2 = 200        # Mass of Star 2
m3 = 250        # Mass of Star 3
G = 1           # Gravitational constant
t1 = 0.0        # Start time
t2 = 2.0        # End time
delta = 1e-3    # Maximum error per unit time

# Function to calculate system of ODEs simultaneously
# Note: u = [r,v], r = [r1,r2,r3], v = [v1,v2,v3]
def f(u):
    r1,r2,r3 = u[0,:]
    fr = u[1,:]
    fv1 = G*m2*(r2 - r1)/(norm(r2 - r1))**3 + G*m3*(r3 - r1)/(norm(r3 - r1))**3
    fv2 = G*m1*(r1 - r2)/(norm(r1 - r2))**3 + G*m3*(r3 - r2)/(norm(r3 - r2))**3
    fv3 = G*m1*(r1 - r3)/(norm(r1 - r3))**3 + G*m2*(r2 - r3)/(norm(r2 - r3))**3
    fv = [fv1,fv2,fv3]
    return array([fr,fv],float)

# Function to perform fourth-order Runge-Kutta
def RK(h,u):
    k1 = h*f(u)
    k2 = h*f(u+0.5*k1)
    k3 = h*f(u+0.5*k2)
    k4 = h*f(u+k3)
    newu = u + (k1+2*k2+2*k3+k4)/6
    return newu

# Create lists for points
tpoints = []
x1points = []
y1points = []
x2points = []
y2points = []
x3points = []
y3points = []

# Initial conditions
t = t1                      # Initial time
h = 1e-3                    # Initial time step
r1 = [3.0,1.0]              # Position of Star 1
r2 = [-1.0,-2.0]            # Position of Star 2
r3 = [-1.0,1.0]             # Position of Star 3
r = array([r1,r2,r3],float)
v0 = [0.0,0.0]              # Initial velocities
v = array([v0,v0,v0],float)
u = array([r,v],float)

# Append initial conditions
tpoints.append(t)
x1points.append(r1[0])
y1points.append(r1[1])
x2points.append(r2[0])
y2points.append(r2[1])
x3points.append(r3[0])
y3points.append(r3[1])

while t < t2:

    # Perform two steps of size h
    ua = RK(h,u)

    ub = RK(h,ua)
    xb = ub[0,:,0]
    yb = ub[0,:,1]

    # Perform one step of size 2h
    uc = RK(2*h,u)
    xc = uc[0,:,0]
    yc = uc[0,:,1]

    # Errors in x and y
    epsx = 1/30*(xc - xb)
    epsy = 1/30*(yc - yb)

    # Euclidean errors
    error = sqrt(epsx**2 + epsy**2)

    for i in range(size(error)):
        if error[i] < 1e-100:
            error[i] = 1e-100

    # Ratios of target accuracy and actual accuracies
    rho = h*delta/absolute(error)

    # Only append points and move on if accuracy is within desired range
    if min(rho)>1:
        tpoints.append(t+h)
        x1points.append(xb[0])
        y1points.append(yb[0])
        x2points.append(xb[1])
        y2points.append(yb[1])
        x3points.append(xb[2])
        y3points.append(yb[2])
        t += h
        u = ua

    # Modify step size
    hprime = h*min(rho)**(1/4)

    if hprime > 2*h:
        hprime = 2*h

    h = hprime

# Plot and show
plot(x1points,y1points)
plot(x2points,y2points)
plot(x3points,y3points)
show()