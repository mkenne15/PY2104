import numpy as np
import matplotlib.pyplot as plt

#Model atmosphere from https://ccmc.gsfc.nasa.gov/models/NRLMSIS~00/

atmo_dat = np.genfromtxt('../Resources/Model_Atmosphere.dat')

m = 4.651734e-26 # mass of an N2 molecule in kg
g = 9.81 # grav accel
k_B = 1.380649e-23

temp = atmo_dat[:,12] #T are in Kelvin already
T = temp[0] # Assuming an isothermal atmosphere, using T at the base.

density = atmo_dat[:,9] #This is number density of N2 from the models
alt = atmo_dat[:,5]*1000 #Data saved as km, so converting to m

model = density[0]*np.exp(-m*g*alt/k_B/T)

fig,ax = plt.subplots(nrows=1,ncols=2,figsize=[8,3],dpi=150)
ax[0].plot(alt/1000,density,label='MRLMSIS Model')
ax[0].plot(alt/1000,model,label='Isothermal Model')
ax[0].legend()
ax[0].set_xlabel(r'Altitude (km)')
ax[0].set_ylabel(r'N2 number density (${\rm m}^{-3}$)')

ax[1].plot(alt/1000,density,label='MRLMSIS Model')
ax[1].plot(alt/1000,model,label='Isothermal Model')
ax[1].legend()
ax[1].set_xlabel(r'Altitude (km)')
ax[1].set_ylabel(r'N2 number density (${\rm m}^{-3}$)')
ax[1].set_yscale("log")
plt.tight_layout()
plt.show()