import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import astropy.units as u
import astropy.constants as c
import warnings
warnings.filterwarnings('ignore')


#Defining arrays
T = np.arange(0,1,0.01)
S = T**3

fig,ax = plt.subplots(nrows=1,ncols=2,figsize=[6,3],dpi=150)
# Plotting VDW Gas    
ax[0].plot(T,S,color='k')
ax[0].plot(T,S+0.1,color='k')
x = 0.9
ax[0].axvline(0.89,ymin=x**3,ymax=x**3+0.1,color='grey',alpha=0.5)
x = x**3
ax[0].axhline(x,xmin=(x-0.1)**(1/3),xmax=x**(1/3),color='grey',alpha=0.5)
for i in range(6):
    x = (x-0.1)**(1/3)
    ax[0].axvline(x-0.01,ymin=x**3,ymax=x**3+0.1,color='grey',alpha=0.5)
    x = x**3
    ax[0].axhline(x,xmin=(x-0.1)**(1/3),xmax=x**(1/3),color='grey',alpha=0.5)
x = (x-0.1)**(1/3)
ax[0].axvline(x-0.01,ymin=x**3,ymax=x**3+0.1,color='grey',alpha=0.5)
x = x**3
ax[0].axhline(x,xmin=0,xmax=x**(1/3),color='grey',alpha=0.5)

#Customising Plot
ax[0].set_ylim(0.0,max(S))
ax[0].axes.get_xaxis().set_ticks([])
ax[0].set_xlim(0,1)
ax[0].axes.get_yaxis().set_ticks([])
ax[0].set_xlabel("Temperature")
ax[0].set_ylabel("Entropy")
ax[0].set_title("S-T diagram")

T = np.arange(0,1,0.01)
S1 = T**3
S2 = T**3.4

ax[1].plot(T,S1,color='k')
ax[1].plot(T,S2,color='k')

x = 0.4
ax[1].vlines(x,ymin=x**3,ymax=x**3.4,color='grey',alpha=0.5)
for i in range(6):
     x = x**3.4
     ax[1].hlines(x,xmin=x**(1/3.4),xmax=x**(1/3),color='grey',alpha=0.5)
     x = x**(1/3)
     ax[1].vlines(x,ymin=x**3,ymax=x**3.4,color='grey',alpha=0.5)

#Customising Plot
ax[1].set_ylim(0,0.5**3.4)
ax[1].axes.get_xaxis().set_ticks([])
ax[1].set_xlim(0,0.5)
ax[1].axes.get_yaxis().set_ticks([])
ax[1].set_xlabel("Temperature")
ax[1].set_ylabel("Entropy")
ax[1].set_title("S-T diagram")

plt.tight_layout()
plt.savefig("../Figures/ThirdLaw.jpg")
plt.show()
