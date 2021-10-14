from math import tan

def f(x):
    return tan(x**2 + 3)**2

N = 10
a = 0.0
b = 1.0
h = (b-a)/N

s = f(a) + f(b)
for k in range(1,N,2):
    s += 4*f(a+k*h)
for k in range(2,N,2):
    s += 2*f(a+k*h)

print(1/3*h*s)