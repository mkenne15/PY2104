import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as c
import astropy.units as u

w = np.arange(0,7e14,1e12)*u.Hz
nu = w/(2*np.pi)
l = c.c/nu
T = 250*u.K
u_1 = 8*np.pi*c.h*nu**3/(c.c**3*(np.exp(c.h*nu/(c.k_B*T))-1))
u_1_l = 8*np.pi*c.h*c.c/(l**5*(np.exp(c.h*c.c/(l*c.k_B*T))-1))

T = 200*u.K
u_2 = 8*np.pi*c.h*nu**3/(c.c**3*(np.exp(c.h*nu/(c.k_B*T))-1))
u_2_l = 8*np.pi*c.h*c.c/(l**5*(np.exp(c.h*c.c/(l*c.k_B*T))-1))

T = 300*u.K
u_3 = 8*np.pi*c.h*nu**3/(c.c**3*(np.exp(c.h*nu/(c.k_B*T))-1))
u_3_l = 8*np.pi*c.h*c.c/(l**5*(np.exp(c.h*c.c/(l*c.k_B*T))-1))

fig,ax = plt.subplots(1,2,figsize=[8,4],dpi=150)
ax[0].plot(nu.value,u_1.value, label = 'T=250 K')
ax[0].plot(nu.value,u_2.value, label = 'T=200 K')
ax[0].plot(nu.value,u_3.value, label = 'T=300 K')
ax[0].set_ylim(0,)

ax[1].plot(l.to(u.micron).value,u_1_l.value, label = 'T=250 K')
ax[1].plot(l.to(u.micron).value,u_2_l.value, label = 'T=200 K')
ax[1].plot(l.to(u.micron).value,u_3_l.value, label = 'T=300 K')
ax[1].set_xlim(0,40)
ax[1].set_ylim(0,)

ax[0].set_xlabel(r"$\nu$ (Hz)")
ax[0].set_ylabel(r"$u(\nu,T)$ (J m$^{-3}$ Hz$^{-1}$)")
ax[0].legend()

ax[1].set_xlabel(r"$\lambda \: {\rm (\mu m)}$")
ax[1].set_ylabel(r"$u(\lambda,T)$ (J m$^{-3}$ m$^{-1}$)")
ax[1].legend()
plt.tight_layout()
plt.savefig("../Figures/Blackbody.png")
plt.show()
