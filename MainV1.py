# -*- coding:utf-8 -*-
#
'''
This is the Ground control system of UAV by Jianwei Guo and his team.
CopyRight 2018, Harbin Institute of Technology
'''
# append path of other module
import sys
sys.path.append('./Resource')
import tkinter as tk
# import tkinter.filedialog
# import tkinter.simpledialog
from Resource import uavinfo
from Resource import connect
from Resource import hud


# GUI Config
# root window
root = tk.Tk(screenName='Ground Control V1.0',baseName='Ground Control V1.0')
# frame in root window
uav_info = uavinfo.UAVinfo()
uav_connect = connect.Connect()
frame_hud = tk.LabelFrame(bg = 'white',text = 'HUD')
# frame_connect = tk.LabelFrame(text = 'connect')
# frame layout
# frame_uavinfo.grid(column = 0, row = 0 , rowspan = 2 ,sticky = tk.N+tk.E+tk.S+tk.W)
uav_info.uavinfolabel(uav_info.frame_uavinfo).grid(column = 0, row = 0 , rowspan = 2 ,sticky = tk.N+tk.E+tk.S+tk.W)
frame_hud.grid(column = 1,row = 0, rowspan =1, sticky = tk.N+tk.E+tk.S+tk.W)
uav_connect.connect_module(parent=uav_connect.frame_connect)
# frame_connect.grid(column = 1 ,row = 1, rowspan = 1, sticky = tk.N+tk.E+tk.S+tk.W)

# mainloop/the last step
root.mainloop()
