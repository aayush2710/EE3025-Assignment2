import numpy as np

def lp_stable_cheb(epsilon,N):
    '''%This function gives the low pass stable filter
        for the Chebyschev approximation based upon
        the design parameters epsilon and N
        H(s) = G/p(s)
        [p,G] = lp_stable_cheb(epsilon,N)
        Analytically obtaining the roots of the Chebyschev polynomial
        in the left half of the complex plane'''

    beta=(((1+epsilon**2)**(0.5)+1)/epsilon)**(1/N)
    r1=( beta**2 -1)/(2*beta)
    r2= (beta**2+1)/(2*beta)
    u= 1
    for n in range(int(N/2)):
        phi= np.pi/2 + (2*n+1)*np.pi/(2*N)
        v= np.array([1,-2*r1*np.cos(phi) , r1**2 * np.cos(phi)**2 + r2**2* np.sin(phi)**2])
        p=np.convolve(v,u,mode='full')
        u=p
    G= np.abs(np.polyval(p,1j))/((1+epsilon**2)**(0.5))
    return p,G

#print(lp_stable_cheb(0.1,6))