import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data_all=np.zeros((71,8,4))
for i in range(5,9):
    data = pd.read_csv('E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab4\class2\A%d-3_1.txt' % (i),
                       sep='\t', skiprows=1, header=None).to_numpy(dtype=float)
    data_all[:,:,i-5]=data[0:71,0:8]
fig1=plt.figure()
for i in range(4):
    plt.plot(data_all[20:,3,i],data_all[20:,7,i])
plt.xlim(0,300)
plt.ylim(0,30)
plt.legend(['A5','A6','A7','A8'])
plt.xlabel('Current Density (mA/$cm^2$)',fontsize=15)
plt.ylabel('EQE (%)',fontsize=15)
plt.show()
fig1.savefig("E:/Files/Year4/Year4.2/OptoDevFab/lab_reports/lab4/latex/7.png", dpi=300, format=None, metadata=None,
            bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto',
            backend=None
            )
fig2=plt.figure()
plt.subplot(1,2,1)
for i in range(4):
    plt.plot(data_all[20:-1,3,i],data_all[20:-1,5,i])
plt.legend(['A5','A6','A7','A8'])
plt.xlabel('Current Density (mA/$cm^2$)',fontsize=15)
plt.ylabel('Current efficiency (cd/A)',fontsize=15)
plt.xlim(0,400)
plt.ylim(0,100)
plt.subplot(1,2,2)
for i in range(4):
    plt.plot(data_all[20:-1,0,i],data_all[20:-1,6,i])
plt.legend(['A5','A6','A7','A8'])
plt.xlabel('Voltage (V)',fontsize=15)
plt.ylabel('Power efficiency (lm/W)',fontsize=15)
plt.xlim(4,10)
plt.ylim(0,100)
plt.show()
fig2.savefig("E:/Files/Year4/Year4.2/OptoDevFab/lab_reports/lab4/latex/8.png", dpi=300, format=None, metadata=None,
            bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto',
            backend=None
            )