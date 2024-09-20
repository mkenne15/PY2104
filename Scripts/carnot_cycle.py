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
V_i = 1*u.m**3
V = np.arange(0.5,2.02,0.01)*u.m**3

plt.figure(figsize=[4,3],dpi=150)
#Plotting the full isotherms & Adiabats
for P_i in P_is:
    P_a = adiabatic(V_i,P_i,V)
    P_isot = isothermal(V_i,P_i,V)
    if P_i == 3.0*u.Pa:
        plt.plot(V,P_a,'C0-',label='Adiabat, $PV^\gamma=const$')
        plt.plot(V,P_isot,'C1--',label='Isotherm, $PV=const$')
    else:
        plt.plot(V,P_a,'C0-',label='')
        plt.plot(V,P_isot,'C1--',label='')

gamma = 5/3
V_A = (P_is[0]/P_is[1])**(1/(gamma-1))
P_A = P_is[1]*V_i/V_A
plt.text(V_A.value,P_A.value,'A')

V_B = V_i
P_B = P_is[1]
plt.text(V_B.value,P_B.value,'B')

V_C = (P_is[1]/P_is[0])**(1/(gamma-1))
P_C = P_is[0]*V_i/V_C
plt.text(V_C.value,P_C.value,'C')

V_D = V_i
P_D = P_is[0]
plt.text(V_D.value,P_D.value-0.8,'D')

# Process A-B
V_temp = np.arange(V_A.value,V_B.value,0.001)*u.m**3
P_temp = isothermal(V_A,P_A,V_temp)
plt.plot(V_temp,P_temp,'k-',label='')

# Process B-C
V_temp = np.arange(V_B.value,V_C.value,0.001)*u.m**3
P_temp = adiabatic(V_B,P_B,V_temp)
plt.plot(V_temp,P_temp,'k-',label='')

# Process C-D
V_temp = np.arange(V_C.value,V_D.value,-0.001)*u.m**3
P_temp = isothermal(V_C,P_C,V_temp)
plt.plot(V_temp,P_temp,'k-',label='')

# Process D-A
V_temp = np.arange(V_D.value,V_A.value,-0.001)*u.m**3
P_temp = adiabatic(V_D,P_D,V_temp)
plt.plot(V_temp,P_temp,'k-',label='')

frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])
plt.xlim(0.5,2)
plt.ylim(0.0,8)
plt.ylabel("Pressure")
plt.xlabel("Volume")
plt.title("Adiabats and Isotherms for\n different initial conditions.")
plt.legend()
plt.tight_layout()
plt.savefig("../Figures/Carnot_Cycle.jpg")
plt.show()
