# Exercise 9.5: FTCS solution of the wave equation
# Ryan Hennessey

from numpy import zeros,empty
from math import exp
from pylab import plot,xlabel,ylabel,show

# Constants
v = 100.0       # 100 [m*s^-1]
L = 1.0         # String length [m]
d = 0.10        # Distance from end of string [m]
C = 1.0         # [m*s^-1]
sigma = 0.3     # [m]
N = 100         # Number of divisions in grid
a = L/N         # Grid spacing
h = 1e-6        # Time-step [s]
epsilon = h

t1 = 0.0
t2 = .01
t3 = .02
t4 = .03
tend = 1.00      # End of time interval [s]

# Create arrays
phi = zeros(N+1,float)
phinew = empty(N+1,float)
phinew[0] = 0.0
phinew[N] = 0.0
psi = empty(N+1,float)
for x in range(N+1):
    psi[x] = C*.01*x*(L - .01*x)/L**2*exp(-(.01*x - d)**2/(2*sigma**2))
psinew = empty(N+1,float)
psinew[0] = 0.0
psinew[N] = 0.0

plot(psi)
# Main loop
t = 0.0
while t < tend:

    # Calculate new values for phi, psi
    phinew[1:N] = phi[1:N] + h*psi[1:N]
    psinew[1:N] = psi[1:N] + h*v**2/a**2*(phi[0:N-1]+phi[2:N+1]-2*phi[1:N])
    phi,phinew = phinew,phi
    psi,psinew = psinew,psi
    t += h

    # Make plots at the given times
    if abs(t - t1) <= epsilon:
        plot(.01*psi)
    if abs(t - t2) <= epsilon:
        plot(.01*psi)
    if abs(t - t3) <= epsilon:
        plot(.01*psi)
    if abs(t - t4) <= epsilon:
        plot(.01*psi)


xlabel("Length along string, x [cm]")
ylabel("Displacement, psi [cm]")
show()