import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../Resources/L_T_water.csv")
plt.figure(figsize=[4,3], dpi=150)
plt.plot(data.Temp,data.L)
plt.xlabel(r"T ($^{\rm o}$ C)")
plt.ylabel(r"L$_{12}$ (kW/kg)")
plt.xlim(0,373.15)
plt.ylim(0,)
plt.tight_layout()
plt.savefig("../Figures/Vapourisation_Energy_Time_Water.jpg")
plt.show()
