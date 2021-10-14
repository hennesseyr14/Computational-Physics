# FINAL EXAM, v.2
# Number 8
# Ryan Hennessey

from numpy import array,copy,empty

A = array([[ 0,  3, -1,  4 ],
           [ 2,  1,  5, -1 ],
           [-1,  0,  2,  3 ],
           [-4,  1,  1,  1 ]], float)
v = array([-13, 23, -7, -3 ],float)
N = len(v)

# Gaussian elimination
for m in range(N):

    # Partial pivoting
    farthest = abs(A[m,m])
    n = m
    for i in range(m+1,N):
        if farthest < abs(A[i,m]):
            farthest = abs(A[i,m])
            n = i
    if n != m:
        Acopy = copy(A)
        A[m,:],A[n,:] = Acopy[n,:],Acopy[m,:]
        v[m],v[n] = v[n],v[m]

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