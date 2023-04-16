import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data_all=np.zeros((71,8,4))
for i in range(5,9):
    data = pd.read_csv('E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab4\class2\A%d-1_1.txt' % (i),
                       sep='\t', skiprows=1, header=None).to_numpy(dtype=float)
    data_all[:,:,i-5]=data[0:71,0:8]
fig,ax1=plt.subplots()


ax1.set_yscale('log')
for i in range(4):
    plt.xlabel('Voltage (V)',fontsize=15)
    ax1.plot(data_all[:,0,i],data_all[:,4,i])
    plt.ylabel('Luminance (cd/$m^2$)',fontsize=15)
plt.legend(['A5','A6','A7','A8'])
ax2 = ax1.twinx()
for i in range(4):
    ax2.plot(data_all[:,0,i],data_all[:,3,i])
    plt.ylabel('Current density ($mA/cm^2$)',fontsize=15)

ax1.arrow(2, 10, -4, 0,
          head_width = 5,head_length=1,ec='black',color='black',
          width = 3)
ax2.arrow(8, 50, 2, 0,
          head_width = 13,head_length=1,ec='black',color='black',
          width = 8)

plt.show()
fig.savefig("E:/Files/Year4/Year4.2/OptoDevFab/lab_reports/lab4/latex/6.png", dpi=300, format=None, metadata=None,
            bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto',
            backend=None
            )