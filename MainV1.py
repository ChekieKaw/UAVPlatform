# -*- coding:utf-8 -*-
# namespace MainV1
# this is the main programm. Creat by Jianwei Guo CopyRight 2018

import tkinter as tk
from Connect import ConnectView as cv
from DataView import DataView as dv

root = tk.Tk()
dataview = dv.DataView()
connectview = cv.ConnectView()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=2)
dataview.posture_view(root).grid(column=0, row=0, sticky=tk.E + tk.W + tk.N + tk.S)
dataview.flightdata_view(root).grid(column=0, row=1, sticky=tk.E + tk.W + tk.N + tk.S)
connectview.connection_view(parent=root).grid(column=1, row=0, rowspan=2, sticky=tk.N + tk.S + tk.W + tk.E)
root.update()
# root.geometry(root.geometry)
root.mainloop()
