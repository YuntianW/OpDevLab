import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
fig=plt.figure()

for i in range(5,9):
    ax = fig.add_subplot(2, 2, i-4)
    ax.set_yscale('log')
    for j in range(1,5):

        data = pd.read_csv('E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab4\class2\A%d-%d_1.txt'%(i,j),
                                        sep='\t', skiprows=1, header=None).to_numpy(dtype=float)

        plt.plot(data[0:70,0],data[0:70,4])
    plt.xlabel('Voltage (V)', fontsize=12)
    plt.ylabel('Luminance (cd/$m^2$)', fontsize=12)
    plt.title('A%d'%(i))
plt.show()
fig.savefig("E:/Files/Year4/Year4.2/OptoDevFab/lab_reports/lab4/latex/5.png", dpi=300, format=None, metadata=None,
            bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto',
            backend=None
            )