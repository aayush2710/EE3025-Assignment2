import numpy as np

def lpbp(p,Omega0,B,Omega_p2):

    '''This function transforms the lowpass stable filter obtained
    from the Chebyschev approximation to the bandpass
    equivalent
    [num,den,G] = lpbp(p,Omega0,B,Omega_p2)
    Omega0 and B are the lowpass-bandpass transformation parameters
    and Omega_p2 is the lower limit of the passband, used
    to evaluate the gain G_bp
    H(s) = G/p(s) is the stable low pass Cheybyschev approximation
    Hbp(s) = G_bp*num(s)/den(s) is the corresponding bandpass stable
    filter'''

    N = len(p);
    const = np.array([1,0,Omega0**2])
    v = const
    if N > 2:
        
        for i in range(1,N) :
            M = len(v)
            v(M-i) = v(M-i) + p(i+1)*B^i
            if i < N-1 :
                v = np.conv(const,v)
   

        den = v;

    elif N==2 :

        M = len(v);
        v(M-1) = v(M-1) + p(N)*B;
        den = v;
        
    else :
        den = p;

   

    num = np.concatenate((np.array([1]),np.zeros(N-1)))
    G_bp = abs(np.polyval(den,1j*Omega_p2)/(np.polyval(num,1j*Omega_p2)))
    return num,den,G_bp 