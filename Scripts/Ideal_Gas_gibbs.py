import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import astropy.units as u
import astropy.constants as c
import warnings
warnings.filterwarnings('ignore')

#Defining equations of state
def Ideal_gas(V,T,a,b):
    P = c.R*T*u.mol/(V)
    return P
    
def Ideal_gas_Gibbs(V,T,P,a,b):
    G = 1*u.J-c.R*T*u.mol*np.log((V).value) + P*V
    return G

#Defining arrays
T_VDW = np.arange(21,250,2)*u.K
V_VDW = np.arange(0.1,2.02,0.0001)*u.m**3
a = 1e2*u.J*u.m**3
b = 0.1*u.m**3
T_c = 8*a/(27*c.R*b*u.mol)
P_c = a/(27*b**2)
V_c = 3*b

P_VDW = Ideal_gas(V_VDW,0.9*T_c,a=a,b=b)
G_VDW = Ideal_gas_Gibbs(V_VDW,0.9*T_c,P_VDW,a=a,b=b)
#G_VDW = 1*u.J-c.R*0.9*T_c*u.mol*np.log((V_VDW-b).value)-a/V_VDW + P_VDW*V_VDW

fig,ax = plt.subplots(nrows=2,ncols=1,figsize=[3,6],dpi=150)
# Plotting VDW Gas    
ax[0].plot(P_VDW,V_VDW ,color='k')

ax[1].plot(P_VDW,G_VDW ,color='k')

#Customising Plot
ax[0].set_ylim(0.0,2)
ax[0].axes.get_xaxis().set_ticks([])
ax[0].set_xlim(140,350)
ax[0].axes.get_yaxis().set_ticks([])
ax[0].set_xlabel("Pressure")
ax[0].set_ylabel("Volume")
ax[0].set_title("P-V diagram")

ax[1].set_ylim(60,400)
ax[1].axes.get_xaxis().set_ticks([])
ax[1].set_xlim(140,350)
ax[1].axes.get_yaxis().set_ticks([])
ax[1].set_xlabel("Pressure")
ax[1].set_ylabel("Gibbs")

ax[1].set_title("Pressure vs Gibbs Free Energy")
plt.tight_layout()
plt.savefig("../Figures/Ideal_behaviour.jpg")
plt.show()
