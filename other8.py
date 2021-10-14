from numpy import array,copy,empty

A = array([[ 0,  3, -1,  4 ],
           [ 2,  1,  5, -1 ],
           [-1,  0,  2,  3 ],
           [-4,  1,  1,  1 ]], float)
v = array([-13, 23, -7, -3 ],float)
N = len(v)

# Pivoting
i = 1
while A[0,0] == 0:
    Acopy = copy(A)
    A[0,:],A[i,:] = Acopy[i,:],Acopy[0,:]
    v[0],v[i] = v[i],v[0]
    i += 1

#Acopy = copy(A)
#A[0,:],A[3,:] = Acopy[3,:],Acopy[0,:]

# Gaussian elimination
for m in range(N):

    print(A)

    # Divide by the diagonal element
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    # Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

# Backsubstitution
x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

print(x)