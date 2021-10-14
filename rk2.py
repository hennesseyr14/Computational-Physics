from math import tanh

def f(x,t):
    return 1 - x**2*tanh(t)

a = 0
b = 1
N = 10
h = (b-a)/N

x = 0
for step in range(2):
    t = step*h
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    x += k2
    print(t,k1,k2,x)