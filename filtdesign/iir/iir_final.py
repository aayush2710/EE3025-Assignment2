#IIR  FILTER DESIGN USING THE CHEBYSCHEV APPROXIMATION
#The order of the filter is N = 4
#Getting values of the various analog and digital filter parameters
import numpy as np
from lp_stable_cheb import *
from lpbp import *
from bilin import * 
import matplotlib.pyplot as plt
#The chebyschev filter parameter (epsilon) obtained
#from the given constraints

epsilon = 0.4;

'''The analog lowpass filter'''

p,G_lp = lp_stable_cheb(epsilon,N)
Omega_L = np.arange(0,2.01,0.01)
H_analog_lp = G_lp*np.abs(1/np.polyval(p,1j*Omega_L))
# plt.plot(Omega_L,H_analog_lp);
# plt.xlabel('\Omega')
# plt.ylabel('|H_{a,LP}(j\Omega)|')
# plt.show()

'''The analog bandpass filter'''

num,den,G_bp = lpbp(p,Omega_0,B,Omega_p1)
Omega = np.arange(-0.65,0.66,0.01)
H_analog_bp = G_bp*np.abs(np.polyval(num,1j*Omega)/np.polyval(den,1j*Omega))
# plt.plot(Omega,H_analog_bp);
# plt.xlabel('\Omega')
# plt.ylabel('|H_{a,BP}(j\Omega)|')
# plt.show()
# plt.savefig('../figs/iir/BP_analog.eps')
# plt.savefig('../figs/iir/BP_analog.pdf')




'''The digital bandpass filter'''

dignum,digden,G = bilin(den,omega_p1)
omega = np.arange(-2*np.pi/5,2*np.pi/5+np.pi/1000,np.pi/1000)
H_dig_bp = G*np.abs(np.polyval(dignum,np.exp(-1j*omega))/np.polyval(digden,np.exp(-1j*omega)))
plt.plot(omega/np.pi,H_dig_bp)
plt.xlabel('\omega/\pi')
plt.ylabel('|H_{d,BP}(\omega)|')
plt.show()
iir_num = G*dignum
iir_den = digden

# np.savetxt('digden.dat',digden,delimiter=',')
# np.savetxt('iir_num.dat',iir_num,delimiter=',')
# np.savetxt('iir_den.dat',iir_den,delimiter=',')
# np.savetxt('dignum.dat',dignum,delimiter=',')
# np.savetxt('G.dat',G,delimiter=',')
