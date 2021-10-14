# 8.16  The three-body problem, b)
# Ryan Hennessey

from numpy.linalg import norm
from numpy import array,sqrt,absolute,size
from visual import sphere,color,display,rate

# Constants (in arbitrary units)
m1 = 150.0        # Mass of Star 1
m2 = 200.0        # Mass of Star 2
m3 = 250.0        # Mass of Star 3
G = 1.0           # Gravitational constant
t1 = 0.0        # Start time
t2 = 2.0       # End time
delta = .001    # Maximum error per unit time

# Function to calculate system of ODEs simultaneously
# Note: u = [r,v], r = [r1,r2,r3], v = [v1,v2,v3]
def f(u):
    r1,r2,r3 = u[0,:]
    fr = u[1,:]
    fv1 = G*m2*(r2 - r1)*(norm(r2 - r1))**-3 + G*m3*(r3 - r1)*(norm(r3 - r1))**-3
    fv2 = G*m1*(r1 - r2)*(norm(r1 - r2))**-3 + G*m3*(r3 - r2)*(norm(r3 - r2))**-3
    fv3 = G*m1*(r1 - r3)*(norm(r1 - r3))**-3 + G*m2*(r2 - r3)*(norm(r2 - r3))**-3
    fv = [fv1,fv2,fv3]
    return array([fr,fv],float)

# Function to perform fourth-order Runge-Kutta
def RK(h,u):
    k1 = h*f(u)
    k2 = h*f(u+0.5*k1)
    k3 = h*f(u+0.5*k2)
    k4 = h*f(u+k3)
    newu = u + (k1+2*k2+2*k3+k4)/6.0
    return newu

# Initial conditions
t = t1                      # Initial time
h = 1e-3                    # Initial time step
r1 = [3.0,1.0,0.0]              # Position of Star 1
r2 = [-1.0,-2.0,0.0]            # Position of Star 2
r3 = [-1.0,1.0,0.0]             # Position of Star 3
r = array([r1,r2,r3],float)
v0 = [0.0,0.0,0.0]              # Initial velocities
v = array([v0,v0,v0],float)
u = array([r,v],float)

d = display()

# Create stars
Star1 = sphere(radius=.0001*m1,pos=r1,color=color.blue)
Star2 = sphere(radius=.0001*m2,pos=r2,color=color.orange)
Star3 = sphere(radius=.0001*m3,pos=r3,color=color.green)



while t < t2:

    rate(50)

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
    epsx = (xc - xb)*(30.0)**-1
    epsy = (yc - yb)*(30.0)**-1

    # Euclidean errors
    error = (epsx**2 + epsy**2)**0.5

    for i in range(size(error)):
        if error[i] < 1e-100:
            error[i] = 1e-100

    # Ratios of target accuracy and actual accuracies
    rho = h*delta*(absolute(error))**-1

    # Only append points and move on if accuracy is within desired range
    if min(rho)>=1:
        Star1.pos = ub[0,0,:]
        Star2.pos = ub[0,1,:]
        Star3.pos = ub[0,2,:]

        t =t + h
        u = ua

    # Modify step size
    hprime = h*min(rho)**.25

    if hprime >= 2*h:
        hprime = 2*h

    h = hprime