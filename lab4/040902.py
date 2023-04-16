import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.constants
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d


PD_res_data = pd.read_csv('E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab4\PD_response.txt',
                          sep='\t', skiprows=0, header=None).to_numpy(dtype=float)
luminance_data = pd.read_csv('E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab4\Luminance.txt',
                             sep='\t', skiprows=0, header=None).to_numpy(dtype=float)
group_num = 5
spectrum_data = pd.read_csv('E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab4\class2\A%d-PL.txt' % (group_num),
                            sep='\t', skiprows=17, header=None).to_numpy(dtype=float)
sweep_data = pd.read_csv('E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace\lab4\class2\A%d-1_1.txt'%(group_num),
                         sep='\t', skiprows=1, header=None).to_numpy(dtype=float)
wavelength = spectrum_data[506:1521, 0]
spectrum = spectrum_data[506:1521, 1]
PD_res_func = interp1d(PD_res_data[:, 0], PD_res_data[:, 1])
PD_res = PD_res_func(wavelength)
luminance_func = interp1d(luminance_data[:, 0], luminance_data[:, 2])
luminance = luminance_func(wavelength)
wavelength = wavelength * 1e-9
absorbsion=0.8
A=4e-6
int_lumi = np.trapz(spectrum, wavelength)
spectrum_norm = spectrum / int_lumi
# wavelength=wavelength*1e-9
I_PD = sweep_data[:71, 2]
x = I_PD / np.trapz(spectrum_norm * PD_res, wavelength)/absorbsion
num_photons = x * np.trapz(spectrum_norm / (scipy.constants.h * scipy.constants.c / wavelength), wavelength)
I_input = sweep_data[:71, 1]
J=I_input/A/1e1
num_electron = I_input / scipy.constants.elementary_charge
EQE = num_photons / num_electron * 100
Flux=x*np.trapz(spectrum_norm*luminance,wavelength)
lum_intensity=Flux/np.pi
L=lum_intensity/(A)
V=sweep_data[:71, 0]
Power_eff=Flux/(I_input*V)
Current_eff=lum_intensity/I_input
# fig=plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.set_yscale('log')
# plt.plot(V,L)
# plt.show()