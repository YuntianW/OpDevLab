import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os
dir='E:/Files/Year4/Year4.2/OptoDevFab/lab_reports/lab1/2023LAB2/2023LAB2/'
list=os.listdir(dir)
seq=np.array([4,5,6,7])
pres=np.array([ 3.50, 4.5, 6.5, 10])*0.1
fig=plt.figure()
for i in range(0,len(seq)):
    data=pd.read_csv(dir+list[seq[i]],sep='\t',skiprows=17,header=None)
    data=data.drop(data.shape[0]-1).to_numpy(dtype=float)

    plt.plot(data[:,0],data[:,1])
    plt.ylim(bottom=0,top=100)
    plt.xlim((400,800))
plt.xlabel('Wavelenth/nm',fontsize=18)
plt.ylabel('Intensity/%',fontsize=18)
plt.legend([ 0.35, .45, .65, 1])
plt.show()
fig.savefig("E:/Files/Year4/Year4.2/OptoDevFab/lab_reports/lab1/template/12.png", dpi=1200, format=None, metadata=None,
            bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto',
            backend=None
            )