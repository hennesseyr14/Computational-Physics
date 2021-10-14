from math import exp

def f(x):
    return 5/(3+exp(x))

x = 1

for i in range(12):
    oldx = x
    x = f(x)
    print(x)

print(3*x+x*exp(x))
print(x-oldx)