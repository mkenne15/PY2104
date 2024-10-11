import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2,0.01)
Z = 2*np.cosh(x)
P_aligned = np.exp(x)/Z
P_antialigned = np.exp(-x)/Z

plt.figure(figsize=[4,3],dpi=150)
plt.plot(x,P_aligned,'--',label='P(parallel)')
plt.plot(x,P_antialigned,'-.',label='P(anti-parallel)')
plt.ylabel("Probability")
plt.xlabel("x = $\mu B/ k T$")
plt.legend()
plt.xlim(0,2)
plt.tight_layout()
plt.savefig("../Figures/x_versus_prob.png")
plt.show()
