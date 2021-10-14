from numpy import arange,sin,cos,pi,linspace
from pylab import plot,show

omega = 1
t = linspace(0,2*pi*omega,100)
y = .5 * sin(omega*t) + 1/pi + -2/(3*pi)*cos(2*omega*t) + -2/(8*pi)*cos(3*omega*t)

plot(t,y)
show()
