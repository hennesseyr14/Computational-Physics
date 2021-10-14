from numpy import linspace,sqrt,cos,pi
from pylab import plot,show

# Plottin some stuff 4 fizzix

psi = linspace(0,pi,100)
y = cos(psi)

# Est-ce que ca comment je prends un note dans ma programme ?

for a in (1,2,4,12):
    ratio = (1 + a)**-2 * (2*y**2 + a**2 - 1 + 2*y*sqrt(a**2 + y**2 - 1))
    plot(psi,ratio)

show()


