import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab2\Class 2lab2\Class 2lab2\A56-R_CAL.txt',
                    sep='\t', skiprows=2, header=None).to_numpy(dtype=float)
plt.figure()
plt.plot(data1[:, 0], data1[:, 1])
plt.plot(data1[:, 2], data1[:, 3])
plt.show()
data2 = pd.read_csv('E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab2\Class 2lab2\Class 2lab2\A57-R_CAL.txt',
                    sep='\t', skiprows=1, header=None).to_numpy(dtype=float)
plt.figure()
plt.plot(data2[:, 0], data2[:, 1])
plt.plot(data2[:, 2], data2[:, 3])
plt.show()
