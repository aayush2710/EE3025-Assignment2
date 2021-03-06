import numpy as np

'''The function
[C K] = lattice(N,D)
computes the lattice parameters K and the ladder parameters C for the
system function H(z) = N(z)/D(z), where both the numerator and denominator
are of the same order'''

c = np.loadtxt('dignum.dat')
v = np.loadtxt('digden.dat')

u = np.flip(v)

m = len(v)
K = np.zeros(m)
K[m-2] = v[m-1]
C = np.zeros(m)
C[m-1] = c[m-1]

while m > 1 and K[m-2] != 1:    
    c = c - C[m-1]*u
    v = (v - K[m-2]*u)/(1 - K[m-2]**2)
    m = m - 1
    v = v[:m]
    c = c[:m]

    u = np.flip(v)
    
    if m > 1:
        K[m-2] = v[m-1]
    C[m-1] = c[m-1]
print(C,K)