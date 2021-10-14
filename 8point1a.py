# Exercise 8.1: A low-pass filter
# Ryan Hennessey

from numpy import arange
from pylab import plot,xlabel,ylabel,show

def V_in(t):
    if int(2*t)%2 == 0:
        return 1
    else:
        return -1

def f(RC,V_out,t):
    return 1/RC*(V_in(t) - V_out)

a = 0.0         # Start of the interval
b = 10.0        # End of the interval
N = 1000        # Number of steps
h = (b-a)/N     # Size of a single step

tpoints = arange(a,b,h)

RC = .01

# Calculate and graph V_out(t) for RC = .01, .1, 1
# using fourth-order Runge-Kutta
while RC <= 1:
    V_outpoints = []
    V_out = 0.0     # Initial condition

    for t in tpoints:
        V_outpoints.append(V_out)
        k1 = h*f(RC,V_out,t)
        k2 = h*f(RC,V_out+0.5*k1,t+0.5*h)
        k3 = h*f(RC,V_out+0.5*k2,t+0.5*h)
        k4 = h*f(RC,V_out+k3,t+h)
        V_out += (k1+2*k2+2*k3+k4)/6

    plot(tpoints,V_outpoints)
    xlabel("t")
    ylabel("V_out(t)")

    RC *= 10

show()