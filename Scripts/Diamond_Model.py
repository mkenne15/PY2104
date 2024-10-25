import numpy as np
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

plt.figure(figsize=[4,3], dpi=150)
plt.plot(temp,Cv,'.',label='Experimental Data')
plt.axhline(3*c.R.value,linestyle='--')
plt.text(200,25.5, '3R')
plt.xlabel(r"T (K)")
plt.ylabel(r"C$_{\rm V}$ (J/K/mol)")
plt.ylim(0,27.5)
plt.xlim(0,1325)
plt.legend()
plt.tight_layout()
plt.savefig("../Figures/Diamond_Data.jpg")
plt.show()
