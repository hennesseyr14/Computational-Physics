# 7.9   Image deconvolution, c)
# Ryan Hennessey

from pylab import imshow,gray,show
from numpy import loadtxt,exp,zeros
from numpy.fft import rfft2,irfft2

# Width of Gaussian
sigma = 23.5

# Load data
data = loadtxt("blur.txt",float)

# Get dimensions of data array
r,c = data.shape

# Create zero matrix for point spread
density = zeros([r,c],float)

# Gaussian point spread function
def f(x,y):
    return exp(-(x**2 + y**2)/(2*sigma**2))

# Calculate density at each point, bearing in mind that point
# spread function is periodic
for x in range(0,c//2):
    for y in range(0,r//2):
        density[x,y] = f(x,y)
    for y in range(r//2,r):
        density[x,y] = f(x,y-r)
for x in range(c//2,c):
    for y in range(0,r//2):
        density[x,y] = f(x-c,y)
    for y in range(r//2,r):
        density[x,y] = f(x-c,y-r)

# Take Fourier transform of both blurred photo and
# point spread function
ftdata = rfft2(data)
ftdensity = rfft2(density)

# Divide one by the other
div = ftdata
epsilon = 1e-3

for i in range(c):
    for j in range(r//2+1):
        if ftdensity[i,j]>=epsilon:
            div[i,j] /= ftdensity[i,j]

# Perform an inverse transform to get the unblurred photo
photo = irfft2(div)

# Display the unblurred photo on the screen
imshow(photo)
gray()
show()