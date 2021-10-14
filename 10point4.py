# Exercise 10.4: Radioactive decay again
# Ryan Hennessey

from numpy import log,arange,exp,sort,size
from random import random
from pylab import plot,xlabel,ylabel,show

# Constants
NTl = 1000          # Number of thallium atoms
tau = 3.053*60      # Half life of thallium in seconds
mu = log(2/tau)     # Coefficient
h = 1.0             # Size of time step in seconds
tmax = 1000         # Total time

xlist = []
tpoints = arange(0.0,tmax,h)
Tlpoints = []

for i in range(NTl+1):
    z = random()
    x = -1/mu*log(1-z)
    xlist.append(x)

plist = mu*exp(-mu*xlist)

decay = sort(plist)

for t in tpoints:
    for decay in plist:
        if decay < t:
            NTl -= 1

    Tlpoints.append(NTl)

# Make the graph
plot(tpoints,Tlpoints)
xlabel("Time")
ylabel("Number of atoms")
show()