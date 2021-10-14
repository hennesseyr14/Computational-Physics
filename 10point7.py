# 10.7: Volume of a hypersphere
# Ryan Hennessey

from numpy import empty
from random import random

N = 1000000     # Number of points
d = 10          # Dimension of hypersphere
V = 2**d        # Volume from which sample points are taken

# Function that returns 1 if r is within sphere, 0 otherwise
def f(r):
    sum = 0
    for i in range(d):
        sum += r[i]**2
    if sum <= 1:
        return 1
    else:
        return 0

# Main loop
count = 0
for j in range(N+1):
    r = empty(d)
    for i in range(d):
        r[i] = random()
    count += f(r)

# Calculate and print integral
I = V/N*count
print(I)