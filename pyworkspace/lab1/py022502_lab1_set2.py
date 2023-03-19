import numpy as np
import matplotlib.pyplot as plt

pres=np.array([ 3.5, 4.5, 6.5, 10])*0.1
thickness=np.array([89.27, 92.41, 86.58, 61.25])
resistance=np.array([87, 104, 133, 1e6])
# fig1=plt.figure()
fig, ax1 = plt.subplots()

# ax1.plot(t, R_interp_normalized)
ax1.plot(pres,thickness)
plt.legend(['Thickness'],loc='lower right')
plt.xlabel('Process pressure/Pa',fontsize=18)
plt.ylabel('IZO film thickness/nm',fontsize=18)
# plt.title('IZO film thickness and resistance relationship to O2 gas flow')
ax2 = ax1.twinx()
ax2.plot(pres,resistance,'orange')
ax2.set_yscale('log')
plt.ylabel('surface resistance/$\Omega$',fontsize=18)
plt.legend(['Resistance'],loc='upper left')
plt.show()
fig.savefig("E:/Files/Year4/Year4.2/OptoDevFab/lab_reports/lab1/template/11.png", dpi=600, format=None, metadata=None,
            bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto',
            backend=None
            )