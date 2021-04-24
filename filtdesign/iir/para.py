import numpy as np
import math as mp

Fs=48
L=114
pi = np.pi
'''Constant used to get the normalized digital freqencies'''
const = 2*pi/Fs;

'''The permissible filter amplitude deviation from unity'''
delta = 0.15;

'''Bandpass filter specifications (kHz)'''

'''Passband F_p2 < F_p1'''
F_p1 = 3 + 0.6*(L-107)
F_p2 = 3 + 0.6*(L-109)

'''Stopband F_s2 < F_p21; F_p1 < F_s1'''
F_s1 = F_p1 + 0.3
F_s2 = F_p2 - 0.3

'''Normalized digital filter specifications (radians/sec)'''
omega_p1 = const*F_p1
omega_p2 = const*F_p2

omega_s1 = const*F_s1
omega_s2 = const*F_s2

'''The analog bandpass filter (design) frequencies 
obtained using the bilinear transformation'''
Omega_p1 = np.tan(omega_p1/2)
Omega_p2 = np.tan(omega_p2/2)

Omega_s1 = np.tan(omega_s1/2)
Omega_s2 = np.tan(omega_s2/2)

'''The analog bandpass-lowpass (design) transformation
parameters'''
Omega_0 = np.sqrt(Omega_p1*Omega_p2)
B = Omega_p1 - Omega_p2

'''The lowpass Chebyschev approximation stopband frequency'''
Omega_Ls = min(np.abs((Omega_s1**2 - Omega_0**2)/(B*Omega_s1)),np.abs((Omega_s2**2 - Omega_0**2)/(B*Omega_s2)))

'''The lowpass Chebyschev approximation'''
D1 = 1/((1-delta)**2) - 1
D2 = 1/(delta**2) -1

'''Estimated lowpass Chebyschev filter order'''
N= mp.ceil(mp.acosh(np.sqrt(D2/D1))/mp.acosh(Omega_Ls))

'''Range Of the Chebyschev filter parameter epsilon'''
epsilon1=np.sqrt(D2)/np.cosh(N*mp.acosh(Omega_Ls))
epsilon2= np.sqrt(D1)

print(D1,D2,N,epsilon1,epsilon2,Omega_Ls)