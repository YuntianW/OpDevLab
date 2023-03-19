import numpy as np
import matplotlib.pyplot as plt

oxy=np.array([0, 1, 2, 3, 6, 9])
thickness=np.array([92.41, 84.58, 80.31, 77.53, 53.15, 57.51])
resistance=np.array([104, 161, 4480, 1e6,1e6,1e6])
# fig1=plt.figure()
fig, ax1 = plt.subplots()

# ax1.plot(t, R_interp_normalized)
ax1.plot(oxy,thickness)
plt.legend(['Thickness'],loc='lower right')
plt.xlabel('O2 gas flow/sccm',fontsize=18)
plt.ylabel('IZO film thickness/nm',fontsize=18)
# plt.title('IZO film thickness and resistance relationship to O2 gas flow')
ax2 = ax1.twinx()
ax2.plot(oxy,resistance,'orange')
ax2.set_yscale('log')
plt.ylabel('surface resistance/$\Omega$',fontsize=18)
plt.legend(['Resistance'],loc='upper left')
plt.show()
fig.savefig("E:/Files/Year4/Year4.2/OptoDevFab/lab_reports/lab1/template/9.png", dpi=600, format=None, metadata=None,
            bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto',
            backend=None
            )