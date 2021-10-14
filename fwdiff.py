from math import tan

a = 0
b = 1
N = 10
h = (b - a)/N

def f(x):
    return tan(x**2 + 3)**2

x = 0

dfdx = (f(x+h)-f(x))/h

print(dfdx)