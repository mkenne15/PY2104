import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.001,1.001,0.002)
S = -(x*np.log(x)+(1-x)*np.log(1-x))

plt.figure(figsize=[4,3],dpi=200)
plt.plot(x,S)
plt.axhline(np.log(2),linestyle='--',color='grey',alpha=0.5)
plt.text(0,np.log(2)+0.03,"ln(2)")
plt.ylim(0.,0.8)
plt.xlabel("x")
plt.ylabel(r"$\Delta$S / (N $k_{\rm B})$")
plt.tight_layout()
plt.savefig("../Figures/Entropy_Mixing_Plot.png")
plt.show()
