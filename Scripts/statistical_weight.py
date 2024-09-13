import matplotlib.pyplot as plt
import numpy as np

def stat_weight(n,N):
    return np.math.factorial(int(N))/(np.math.factorial(n)*np.math.factorial(int(N-n)))

N = 9.0
n = np.arange(0,9.1,1)
omega = np.zeros_like(n)
for i in n:
    omega[int(i)] = stat_weight(i,N)
    

plt.figure(figsize=[3,2],dpi=150)
plt.plot(n,omega)
plt.xlabel("n")
plt.ylabel("$\Omega (n)$")
plt.tight_layout()
plt.savefig("../Figures/Stat_weight.png")
plt.show()