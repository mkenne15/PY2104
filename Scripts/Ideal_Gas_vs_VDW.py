import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import astropy.units as u
import astropy.constants as c
import warnings
warnings.filterwarnings('ignore')

#Defining equations of state
def ideal_gas(V,T):
    P = c.R*T/V*u.mol
    return (P)

def VDW_gas(V,T,a,b):
    P = c.R*T*u.mol/(V-b)-a/V**2
    return P

#Defining arrays
T_Ideal = np.arange(1,250,5)*u.K
V_Ideal = np.arange(0.01,1.02,0.0001)*u.m**3
T_VDW = np.arange(21,250,2)*u.K
V_VDW = np.arange(0.1,1.02,0.0001)*u.m**3
a = 1e2*u.J*u.m**3
b = 0.1*u.m**3
T_c = 8*a/(27*c.R*b*u.mol)
P_c = a/(27*b**2)
V_c = 3*b

fig,ax = plt.subplots(nrows=1,ncols=2,figsize=[6,3],dpi=150)
# Plotting Ideal Gas
for T_i in T_Ideal:
    P_ideal = ideal_gas(V_Ideal,T_i)
    ax[0].plot(V_Ideal,P_ideal,'-',c=cm.hot(T_i/len(T_Ideal)),label='')
# Plotting VDW Gas    
for T_i in T_VDW:
    P_VDW = VDW_gas(V_VDW,T_i,a=a,b=b)
    im = ax[1].plot(V_VDW,P_VDW,'-',c=cm.hot(T_i/len(T_VDW)),label='')
ax[1].plot(V_VDW, VDW_gas(V_VDW,T_c,a=a,b=b),color='C1')
ax[1].plot(V_c,P_c,'k.')
ax[1].axvline(0.1,color='grey',alpha=0.5)
ax[1].text(0.05,500,'b',rotation=90)
    
#Adding colorbar
sm = plt.cm.ScalarMappable(cmap='hot',norm=cm.colors.Normalize(vmin=min(T_VDW.value),vmax=max(T_VDW.value)))
cbar = fig.colorbar(sm, label='T (K)',ax=ax[1])
cbar.set_ticks([])

#Customising Plot
for axes in ax:
    axes.set_xlim(0.0,1)
    axes.axes.get_xaxis().set_ticks([])
    axes.set_ylim(0,1000)
    axes.axes.get_yaxis().set_ticks([])
    axes.set_ylabel("Pressure")
    axes.set_xlabel("Volume")
ax[0].set_title("Ideal Gas")
ax[1].set_title("Van Der Waals Gas")
plt.tight_layout()
plt.savefig("../Figures/Isotherms.jpg")
plt.show()
