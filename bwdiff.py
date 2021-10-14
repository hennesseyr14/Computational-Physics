from math import tan

a = 0
b = 1
N = 10
h = (b - a)/N

def f(x):
    return tan(x**2 + 3)**2

x = 1

dfdx = (f(x)-f(x-h))/h

print(dfdx)