import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import pandas as pd
import astropy.units as u
import astropy.constants as c


#Read in the data
data = pd.read_csv("../Resources/Diamond.csv")

#The Einstein paper has all of the heat capacities in cal/kelvin/mol, so need to hard code a unit conversion
calorie = u.def_unit('calorie', 4.184 * u.J)

#Now, set up arrays and values
temp = data.Temp.values*u.K
Cv = data.Cap.values*(calorie/u.K/u.mol).to(u.J/u.K/u.mol) # Convert Cv to SI

#Finally step is to calculate the heat capacity for the Einstein model, assuming T_E = 1325*u.K
T_E = 1325*u.K
T = np.arange(10,1325,10)*u.K # Making a wide temperature array to evaluate T over
x = T_E/T
Cv_Einstein = 3*c.R*(x**2*np.exp(x)/(np.exp(x)-1)**2)

def f(x):
    #This is simply the function in the integral above
    return x**4*np.exp(x)/(np.exp(x)-1)**2

#First, we need to calculate x_D for all temperatures, assuming T_D = 1800*u.K
T_D = 1800*u.K
x_Ds = T_D/T

#We now need to loop over the integration, for each x_D
Cv_Debye = np.array([])*u.J/u.K/u.mol

for x_D in x_Ds:
    res, err = quad(f, 0.0, x_D) # This numerical integration function returns both the integrated value and an estimate of the error
    Cv_Debye = np.append(Cv_Debye,9*c.R*res/x_D**3)

plt.figure(figsize=[4,3], dpi=150)
plt.plot(temp,Cv,'.',label='Experimental Data')
plt.plot(T,Cv_Einstein,'-',label='Einstein Model')
plt.plot(T,Cv_Debye,'-.',label='Debye Model')
plt.axhline(3*c.R.value,linestyle='--')
plt.text(200,25.5, '3R')
plt.xlabel(r"T (K)")
plt.ylabel(r"C$_{\rm V}$ (J/K/mol)")
plt.ylim(0,27.5)
plt.xlim(0,1325)
plt.legend()
plt.tight_layout()
plt.savefig("../Figures/Debye_Einstein_Model_vs_Data.jpg")
plt.show()
