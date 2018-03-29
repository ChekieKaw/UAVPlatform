# -*- coding:utf-8 -*-
# namespace connect
# this module define the connect part of GCS

import tkinter as tk
import serial

class Connect(tk.LabelFrame):
    link_optionlist = ('com1','com2','com3','com4')
    # GUI part
    frame_connect = tk.LabelFrame(text = 'Connection')

    def __init__(self, master = None):
        tk.Frame.__init__(self,master)
        self.grid()

    def create_optional_menu(self,parent):
        if parent == None:
            parent = tk.LabelFrame(text = 'Connection')
        self.v = tk.StringVar()
        self.v.set(self.link_optionlist)
        self.om = tk.OptionMenu(parent,self.v,*self.link_optionlist)

    def create_connet_button(self,parent=None):
        if parent == None :
            parent = tk.LabelFrame(text = 'Connection')
        connect_button = tk.Button(parent,text = 'Connect',command = None)
        return parent

    def connect_module(self,parent ,frame = None):
#        if frame== None:
#           frame = tk.LabelFrame(parent,text = 'Connection')
        # self.create_connet_button(parent = frame).grid()
        # self.create_optional_menu(parent = frame).grid()
        cn_button = tk.Button(parent = frame , text = 'Connect', command = None)
        cn_button.grid()
        return frame

root = tk.Tk()
uav_connection = Connect()
uav_connection.connect_module(parent= root).grid()
root.mainloop()

