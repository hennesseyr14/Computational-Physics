# Exercise 9.1
# Ryan Hennessey

from numpy import empty,zeros,max
from pylab import imshow,gray,show

# Constants
M = 100         # Grid squares on a side
a = M/100       # Spacing
eps0 = 1        # Permittivity of empty space
target = 1e-6   # Target accuracy

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float)
phiprime = empty([M+1,M+1],float)

# Create array to hold charge density values
rho = zeros([M+1,M+1],float)
for i in range(20,41):
    rho[i,60:81] = 1
for i in range(60,81):
    rho[i,20:41] = -1

# Main loop
delta = 1.0
while delta>target:

    # Calculate new values of the potential
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or i==M or j==0 or j==M:
                phiprime[i,j] = phi[i,j]
            else:
                phiprime[i,j] = (phi[i+1,j] + phi[i-1,j] \
                                 + phi[i,j+1] + phi[i,j-1])/4 + a**2/(4*eps0)*rho[i,j]

    # Calculate maximum difference from old values
    delta = max(abs(phi-phiprime))

    # Swap the two arrays around
    phi,phiprime = phiprime,phi

# Make a plot
imshow(phi)
gray()
show()