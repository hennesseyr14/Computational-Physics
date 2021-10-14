from math import tan

def f(x):
    return tan(x**2 + 3)**2

N = 10
a = 0.0
b = 1.0
h = (b-a)/N

s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s += f(a+k*h)

print(h*s)