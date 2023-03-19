import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog
from matplotlib.patches import Ellipse
from colour_system import cs_hdtv
global cs
cs = cs_hdtv
window = tk.Tk()
window.title('test')
window.geometry('720x700')
global d1, d2, d1_show, d2_show, data

d1 = 20e-9
d2 = 150e-9
d1_show = round(d1 * 1e9)
d2_show = round(d2 * 1e9)

pressed=False
def d1_plus():
    global d1, d1_show

    try:
        d1_show = d1_show + 1
        d1 = d1 + 1e-9
        update_plot()
        l1.config(text=d1_show)
    except:
        pass


def d1_minus():

    global d1, d1_show
    try:
        d1_show = d1_show - 1
        d1 = d1 - 1e-9
        update_plot()
        l1.config(text=d1_show)
    except:
        pass


def d2_plus():
    global d2, d2_show
    try:
        d2 = d2 + 1e-9
        d2_show = d2_show + 1
        update_plot()
        l2.config(text=d2_show)
    except:
        pass


def d2_minus():
    global d2, d2_show
    try:
        d2 = d2 - 1e-9
        d2_show = d2_show - 1
        update_plot()
        l2.config(text=d2_show)
    except:
        pass


def browse_item():
    global data
    file_path = filedialog.askopenfilename(initialdir="E:\Files\Year4\Year4.2\OptoDevFab\pyworkspace")
    l_browse.config(text=file_path)
    data = pd.read_csv(file_path, sep='\t', skiprows=17, header=None)
    data = data.drop(data.shape[0] - 1).to_numpy(dtype=float)

def change_spec():
    global pressed
    try:
        if pressed:
            ellip2.set_visible(False)
            ellip1.set_visible(True)
            pressed = 1 - pressed
            l_which_spec.config(text='Simulation')
        else:
            ellip1.set_visible(False)
            ellip2.set_visible(True)
            pressed = 1 - pressed
            l_which_spec.config(text='Experiment')
        update_plot()
    except:
        pass
b1 = tk.Button(window, text='d1+', width=15, height=1, command=d1_plus, activebackground='red')
b1.pack()
b2 = tk.Button(window, text='d1-', width=15, height=1, command=d1_minus, activebackground='red')
b2.pack()
l1 = tk.Label(window, text=d1_show)
l1.pack()
b3 = tk.Button(window, text='d2+', width=15, height=1, command=d2_plus, activebackground='red')
b3.pack()
b4 = tk.Button(window, text='d2-', width=15, height=1, command=d2_minus, activebackground='red')
b4.pack()
l2 = tk.Label(window, text=d2_show)
l2.pack()
e1 = tk.Entry(window)
b_browse = tk.Button(window, text='browse', width=15, height=1, command=browse_item, activebackground='red')
b_browse.pack()
l_browse=tk.Label(window,text='')
l_browse.pack()
b_change_spec = tk.Button(window, text='change simu or exp spectrum color', width=35, height=1, command=change_spec, activebackground='red')
b_change_spec.pack()
l_which_spec=tk.Label(window,text='Simulation')
l_which_spec.pack()
Ag = pd.read_csv('Lab2-nk-Ag.txt', sep='\t', header=None).to_numpy(dtype=float)
n_Ag_list = Ag[:, 1] + 1j * Ag[:, 2]
Alq = pd.read_csv('Lab2-nk-Alq.txt', sep='\t', header=None).to_numpy(dtype=float)
n_Alq_list = Alq[:, 1] + 1j * Alq[:, 2]
wavelength = Ag[:, 0] * 1e-9

fig = Figure(figsize=(1, 1), dpi=100)

ax = fig.add_subplot(111)
ax.set_xlabel("wavelength")
ax.set_ylabel("Reflectance")
line1, = ax.plot([], [])
line2, = ax.plot([], [])
ellip1 = Ellipse(xy=(0,0), width=29, height=10,color='#FFFFFF')
ax.add_patch(ellip1)
ellip2 = Ellipse(xy=(0,0), width=29, height=10,color='#FFFFFF')
ax.add_patch(ellip2)
ellip2.set_visible(False)

def cal_spectrum():
    global d1, d2
    Reflectance = np.zeros((len(wavelength), 1), dtype=float)
    for i in range(0, len(wavelength)):
        # for i in range(0,1):
        n_Ag = n_Ag_list[i]
        n_Alq = n_Alq_list[i]
        n_air = 1
        t_01 = 2 * n_air / (n_air + n_Ag)
        r_01 = (n_air - n_Ag) / (n_air + n_Ag)
        I_01 = np.array([[1, r_01], [r_01, 1]]) / t_01
        L1 = np.array([[np.exp(-1j * 2 * np.pi * (n_Ag) * d1 / wavelength[i]), 0],
                       [0, np.exp(1j * 2 * np.pi * (n_Ag) * d1 / wavelength[i])]])
        t_12 = 2 * n_Ag / (n_Alq + n_Ag)
        r_12 = (n_Ag - n_Alq) / (n_Alq + n_Ag)
        I_12 = np.array([[1, r_12], [r_12, 1]]) / t_12
        L2 = np.array([[np.exp(-1j * 2 * np.pi * (n_Alq) * d2 / wavelength[i]), 0],
                       [0, np.exp(1j * 2 * np.pi * (n_Alq) * d2 / wavelength[i])]])
        t_23 = 2 * n_Alq / (n_Alq + n_Ag)
        r_23 = (n_Alq - n_Ag) / (n_Alq + n_Ag)
        I_23 = np.array([[1, r_23], [r_23, 1]]) / t_23
        S = I_01 @ L1 @ I_12 @ L2 @ I_23
        r = S[1, 0] / S[0, 0]
        R = r * np.conj(r)
        Reflectance[i] = R
    return Reflectance


def update_plot():
    global cs
    line2.set_data(data[:, 0], data[:, 1])
    x = wavelength * 1e9
    y = cal_spectrum() * 100
    line1.set_data(x, y)

    html_rgb_1 = cs.spec_to_rgb(x, y.flatten(), out_fmt='html')
    min_index_simu = np.argmin(y)
    ax.relim()
    ax.autoscale_view(True, True, True)
    ax.set_ylim(0, 100)
    ax.set_xlim(400, 800)
    ellip1.set_center((x[min_index_simu], y[min_index_simu]))
    ellip1.set_color(html_rgb_1)

    indice = np.where(np.logical_and(data[:, 0] > 380, data[:, 0] < 780))
    lamb = data[np.min(indice):np.max(indice), 0]
    reflectance = data[np.min(indice):np.max(indice), 1]
    min_index = np.argmin(reflectance)
    html_rgb_2 = cs.spec_to_rgb(lamb, reflectance, out_fmt='html')
    ellip2.set_center((lamb[min_index], reflectance[min_index]))
    ellip2.set_color(html_rgb_2)
    # redraw the canvas
    canvas.draw()


canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
window.mainloop()
