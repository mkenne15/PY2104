import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,5,0.01)
m = np.tanh(x)

plt.figure(figsize=[4,3],dpi=150)
plt.plot(x,m)
plt.plot(x,x,'--',alpha=0.5)
plt.ylabel(r"m/$N\mu$")
plt.xlabel("x = $\mu B/ k T$")
plt.axvline(0,linestyle='--',color='grey',alpha=0.5)
plt.axhline(0,linestyle='--',color='grey',alpha=0.5)
plt.xlim(0,5)
plt.ylim(0,1)
plt.tight_layout()
plt.savefig("../Figures/x_versus_m.png")
plt.show()
