# Exercise 10.2: Radioactive decay chain
# Ryan Hennessey

from random import random
from numpy import arange
from pylab import plot,xlabel,ylabel,show

# Constants
NBi213 = 10000                  # Initial number of bismuth 213 atoms
NTl = 0                         # Initial number of thallium atoms
NPb = 0                         # Initial number of lead atoms
NBi209 = 0                      # Initial number of bismuth 209 atoms
tauBi213 = 46.0*60              # Half life of bismuth 213 in seconds
tauTl = 2.2*60                  # Half life of thallium in seconds
tauPb = 3.3*60                  # Half life of lead in seconds
h = 1.0                         # Size of time-step in seconds
pBi213 = 1 - 2**(-h/tauBi213)   # Probability of decay of bismuth 213 in one step
pTl = 1 - 2**(-h/tauTl)         # Probability of decay of thallium in one step
pPb = 1 - 2**(-h/tauPb)         # Probability of decay of lead in one step
pBi213Tl = .0209                # Probability that decayed bismuth 213 will decay to thallium
pBi213Pb = .9791                # Probability that decayed bismuth 213 will decay to lead
tmax = 20000                    # Total time in seconds

# Lists of plot points
tpoints = arange(0.0,tmax,h)
Bi213points = []
Tlpoints = []
Pbpoints = []
Bi209points = []

# Main loop
for t in tpoints:
    Bi213points.append(NBi213)
    Tlpoints.append(NTl)
    Pbpoints.append(NPb)
    Bi209points.append(NBi209)

    # Calculate the number of lead atoms that decay
    decayPb = 0
    for i in range(NPb):
        if random()<pPb:
            decayPb += 1
    NPb -= decayPb
    NBi209 += decayPb

    # Calculate the number of thallium atoms that decay
    decayTl = 0
    for j in range(NTl):
        if random()<pTl:
            decayTl += 1
    NTl -= decayTl
    NPb += decayTl

    # Calculate the number of bismuth 213 atoms that decay
    decayBi213Tl = 0
    decayBi213Pb = 0
    for k in range(NBi213):
        if random()<pBi213:
            if random()<pBi213Tl:
                decayBi213Tl += 1
            else:
                decayBi213Pb += 1
    NBi213 -= decayBi213Tl + decayBi213Pb
    NTl += decayBi213Tl
    NPb += decayBi213Pb

# Make the graph
plot(tpoints,Bi213points)
plot(tpoints,Tlpoints)
plot(tpoints,Pbpoints)
plot(tpoints,Bi209points)
xlabel("Time")
ylabel("Number of atoms")
show()