import numpy as np
import matplotlib.pyplot as plt

kT = np.arange(0.001,10,0.05) #in units of eps

U = -0.5*np.tanh(1/(kT*2))
Cv = (1/(2*kT))**2 * (1/np.cosh(1/(kT*2)))**2
S = U/kT + np.log(2*np.cosh(1/(kT*2)))

fig, ax = plt.subplots(ncols=3,figsize=[12,3],dpi=150)
ax[0].plot(kT,U)
ax[0].set_xlabel(r"$k_{\rm B}T/\epsilon$")
ax[0].set_ylabel(r"$U/\epsilon$")
ax[1].plot(kT,Cv)
ax[1].set_xlabel(r"$k_{\rm B}T/\epsilon$")
ax[1].set_ylabel(r"$C_V/k_{\rm B}$")
ax[2].plot(kT,S)
ax[2].set_xlabel(r"$k_{\rm B}T/\epsilon$")
ax[2].set_ylabel(r"$S/k_{\rm B}$")
plt.tight_layout()
plt.savefig("../Figures/Thermal_properties_2_level.png")
plt.show()
