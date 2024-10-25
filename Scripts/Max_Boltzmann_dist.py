import numpy as np
import matplotlib.pyplot as plt

u = np.arange(0,3,0.01) #in units of eps
F = 4/ np.pi**(1/2) * u**2 * np.exp(-u**2)

fig, ax = plt.subplots(ncols=1,figsize=[3,2],dpi=150)
ax.plot(u,F)
ax.set_xlabel(r"$u = v / \left(\frac{2 k_{\rm B} T}{m}\right)^{1/2}$")
ax.set_ylabel(r"$F_1(u)$")
ax.set_xlim(0,3)
ax.set_ylim(0,0.85)
ax.axvline(1,linestyle='-',color='grey',label=r'$v_{\rm max}$')
ax.axvline(2/np.sqrt(np.pi),linestyle='--',color='grey',label=r'$\langle v \rangle$')
ax.axvline(np.sqrt(3/2),linestyle='-.',color='grey',label=r'$v_{\rm rms}$')
plt.legend()
plt.tight_layout()
plt.savefig("../Figures/Maxwell_Distribution.png")
plt.show()
