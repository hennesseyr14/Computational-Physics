# Exercise 9.4: Thermal diffusion in the Earth's crust
# Ryan Hennessey

from math import sin,pi
from numpy import empty
from pylab import plot,title,xlabel,ylabel,show

# Constants
L = 20.0      # Depth below surface in meters
D = 0.1       # Thermal diffusivity (m^2/day)
N = 100       # Number of divisions in grid
a = L/N       # Grid spacing
h = .1        # Time-step
epsilon = h

A = 10.0      # Constant in Celsius
B = 12.0      # Constant in Celsius
tau = 365.0   # Period in days

Tmid = 10.0   # Intermediate temperature in Celsius
T20 = 11.0    # Temperature at 20 m below surface

t1 = 9.25*tau
t2 = 9.5*tau
t3 = 9.75*tau
t4 = 10.0*tau
tend = t4 + epsilon

# Create arrays
T = empty(N+1,float)
T[N] = T20
T[1:N] = Tmid
Tp = empty(N+1,float)
Tp[N] = T20

# Main loop
t = 0.0
c = h*D/(a*a)
while t<tend:

    # Calculate the new surface temperature values
    T0 = A + B*sin(2*pi*t/tau)
    T[0] = T0
    Tp[0] = T0

    # Calculate the new values of T
    Tp[1:N] = T[1:N] + c*(T[0:N-1]+T[2:N+1]-2*T[1:N])
    T,Tp = Tp,T
    t += h

    # Make plots at the given times
    if abs(t-t1)<epsilon:
        plot(T)
    if abs(t-t2)<epsilon:
        plot(T)
    if abs(t-t3)<epsilon:
        plot(T)
    if abs(t-t4)<epsilon:
        plot(T)

xlabel("x")
ylabel("T")
show()