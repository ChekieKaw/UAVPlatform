# -*- coding:utf-8 -*-
# namespace uavinfo
# this file define the function of information view of UAV GCS

import tkinter as tk
import math
import string

class UAVinfo(tk.LabelFrame):

    altitude = 0.0
    ground_velocity = 0.0
    air_velocity = 0.0
    distant_home = 0.0

    frame_uavinfo = tk.LabelFrame(text='Information')

    def __init__(self,master = None):
        tk.Frame.__init__(self,master)
        self.grid()

    def uavinfolabel(self,parent ,frame = None):
        if frame == None:
            frame = tk.LabelFrame(parent, text='Information')
        # define Lable of information
        info_altitude = tk.Label(frame, text = 'Altitude')
        num_altitude = tk.Label(frame, text = self.altitude)
        info_ground_velocity = tk.Label(frame, text = 'Ground Velocity')
        num_ground_velocity = tk.Label(frame, text = self.ground_velocity)
        info_airvelocity = tk.Label(frame, text = 'Air velocity')
        num_air_velocity = tk.Label(frame, text =self.air_velocity)
        info_distant_home = tk.Label(frame,text = 'Distant from HOME')
        num_distant_home = tk.Label(frame, text = self.distant_home)
        # grid the widgets
        info_altitude.grid(column = 0, row = 0)
        info_airvelocity.grid(column = 0, row = 1)
        info_ground_velocity.grid(column = 0, row = 2)
        info_distant_home.grid(column=0, row = 3)
        num_altitude.grid(column =1 ,row = 0)
        num_ground_velocity.grid(column = 1, row = 1)
        num_air_velocity.grid(column = 1, row = 2)
        num_distant_home.grid(column = 1, row = 3)
        return frame


root = tk.Tk()
uav_info = UAVinfo()
uav_info.uavinfolabel(root).grid()
root.mainloop()



