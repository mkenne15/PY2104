import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import astropy.constants as c

def adiabatic(V_i,P_i,V):
    gamma = 5/3
    return (P_i*V_i**gamma)/(V**gamma)

def isothermal(V_i,P_i,V):
    T = P_i*V_i/c.R
    return (c.R*T/V)

P_is = np.arange(3,5,1)*u.Pa
V = np.arange(0.5,2.02,0.01)

plt.figure(figsize=[4,3],dpi=150)
for P_i in P_is:
    V_i = 1*u.m**3
    P_a = adiabatic(V_i,P_i,V)
    P_isot = isothermal(V_i,P_i,V)
    if P_i == 3.0*u.Pa:
        plt.plot(V,P_a,'C0-',label='Adiabat, $PV^\gamma=const$')
        plt.plot(V,P_isot,'C1--',label='Isotherm, $PV=const$')
    else:
        plt.plot(V,P_a,'C0-',label='')
        plt.plot(V,P_isot,'C1--',label='')
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])
plt.xlim(0.5,2)
plt.ylim(0.0,13)
plt.ylabel("Pressure")
plt.xlabel("Volume")
plt.title("Adiabats and Isotherms for\n different initial conditions.")
plt.legend()
plt.tight_layout()
plt.savefig("../Figures/Adiabats_vs_isotherms.jpg")
plt.show()
