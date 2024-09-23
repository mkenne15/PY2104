import numpy as np
import matplotlib.pyplot as plt

C = 1 #Just setting the heat capacity to a positive number.
T_S_over_T_R = np.arange(0.01,4.05,0.01)
S_R = C*(T_S_over_T_R-1)
S_S = C*np.log(1/T_S_over_T_R)

plt.figure(figsize=[4,3],dpi=150)
plt.plot(T_S_over_T_R,S_R,'--',color='grey',label='Entropy of Reservoir')
plt.plot(T_S_over_T_R,S_S,'-.',color='grey',label='Entropy of System')
plt.plot(T_S_over_T_R,S_S+S_R,'-',color='k',label='Combined Entropy')
plt.ylabel("S")
plt.xlabel(r"$\frac{T_S}{T_R}$")
plt.legend()
plt.xlim(0,4)
plt.tight_layout()
plt.savefig("../Figures/Entropy_Universe_plot.png")
plt.show()
