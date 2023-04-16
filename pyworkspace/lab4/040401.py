import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

fig=plt.figure()


def func(x, a, b, c, d, e, f):
    return a * np.exp(-(x - b) ** 2 / (2 * c ** 2)) + d * np.exp(-(x - e) ** 2 / (2 * f ** 2))


data = np.zeros((2048, 2, 4))
fit_result = np.zeros((4, 7))
for i in range(5, 9):
    data[:, :, i - 5] = pd.read_csv('E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab4\class2\A%d-PL.txt' % (i),
                                    sep='\t', skiprows=17, header=None).to_numpy(dtype=float)
    data1 = data[:, :, i - 5]
    data[:, 1, i - 5] = data1[:, 1] / np.max(data1[:, 1])
    plt.plot(data1[:, 0], data1[:, 1] / np.max(data1[:, 1]))
    xdata = data[:, 0, i - 5]
    ydata = data[:, 1, i - 5]
    popt, pcov = curve_fit(func, xdata, ydata, bounds=([0, 300, 0, 0, 520, 0], [1, 520, 1000, 1, 800, 1000]))
    residuals = ydata - func(xdata, *popt)
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((ydata - np.mean(ydata)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    fit_result[i - 5, :-1] = popt
    fit_result[i - 5, -1] = r_squared
    print(r_squared)
plt.xlabel('Wavelength (nm)', fontsize=18)
plt.ylabel('Intensity a.u.', fontsize=18)
plt.legend(['A5', 'A6', 'A7', 'A8'])
plt.show()
fig.savefig("E:/Files/Year4/Year4.2/OptoDevFab/lab_reports/lab4/latex/4.png", dpi=300, format=None, metadata=None,
            bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto',
            backend=None
            )
