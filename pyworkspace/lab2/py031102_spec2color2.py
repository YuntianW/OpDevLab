import numpy as np
from scipy.constants import h, c, k
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from colour_system import cs_hdtv
import pandas as pd
import os
cs = cs_hdtv
dir='E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab2\Class2_lab2'
list=os.listdir(dir)
data=pd.read_csv(dir+'/'+list[11],sep='\t',skiprows=17,header=None)
# data=pd.read_csv(dir+'/'+list[8],sep='\t',skiprows=17,header=None)
data=data.drop(data.shape[0]-1).to_numpy(dtype=float)

indice=np.where(np.logical_and(data[:,0]>380,data[:,0]<780))
fig,ax=plt.subplots()
lamb=data[np.min(indice):np.max(indice),0]
reflectance=data[np.min(indice):np.max(indice),1]
min_index=np.argmin(reflectance)

plt.plot(lamb,reflectance)
html_rgb=cs.spec_to_rgb(lamb,reflectance,out_fmt='html')
plt.xlim(400,800)
plt.ylim(0,100)
ellip = Ellipse(xy=(lamb[min_index], reflectance[min_index]), width=29,height=10, fc=html_rgb)
ax.add_patch(ellip)
plt.show()

