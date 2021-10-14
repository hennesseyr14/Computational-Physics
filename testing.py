from numpy.linalg import norm
from numpy import array,absolute

r = array([-3.0,4.0,0.0],float)
s = norm(r)
q = absolute(r)

print(s)
print(q)

print(min(r))

x = 1/30
print(x)