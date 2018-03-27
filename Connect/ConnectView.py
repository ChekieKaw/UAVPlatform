# -*- coding:utf-8 -*-

import tkinter as tk
from Connect import ConnectControl
import time


class ConnectView:

    def __init__(self):
        self.time = time.asctime(time.localtime(time.time()))
        self.connect_text_variable = tk.StringVar()
        self.timevariable = tk.StringVar()
        self.get_com = ConnectControl.ConnectControl()
        self.com_state_msg = tk.StringVar()
        self.com_op = tk.StringVar()
        self.baudrate = 0
        self.timeout = None
        self.entry_variable_baudrate = tk.StringVar()
        self.entry_variable_timeout = tk.DoubleVar()
        self.port = ConnectControl.ConnectControl()
        self.connect_button_state = tk.DISABLED
        self.connect_button = tk.Button()
        self.com_op.set(0)
        self.portlist = ()
        self.com_list_om = tk.OptionMenu(None, None, None)

    def connection_view(self,
                        port=None,
                        parent=None,

                        ):
        # define frame
        connection_frame = tk.LabelFrame(parent, text='Connection')
        self.com_state_msg.set('Unavailable!')
        combutton = tk.Button(connection_frame,
                              text='Search COM',
                              command=self.get_COM,
                              state=tk.ACTIVE)

        # connect_find_port result & port chose button (menu)

        com_msg = tk.Label(connection_frame,
                           textvariable=self.com_state_msg)

        self.com_list_om = tk.OptionMenu(connection_frame, self.com_op, *tuple(self.get_com.portlist))
        # setting port parameter
        self.entry_variable_baudrate.set(9600)
        self.entry_variable_timeout.set(None)
        entry_baudrate = tk.Entry(connection_frame, textvariable=self.entry_variable_baudrate)
        entry_timeout = tk.Entry(connection_frame, textvariable=self.entry_variable_timeout)
        lable_baudrate = tk.Label(connection_frame, text='Baudrate')
        lable_timeout = tk.Label(connection_frame, text='Timeout')
        # Connect Button setting
        self.connect_text_variable.set('Open')
        self.connect_button = tk.Button(connection_frame,
                                        default=tk.DISABLED,
                                        textvariable=self.connect_text_variable,
                                        command=self.connect_button_event,
                                        state=self.connect_button_state)
        self.connect_button.setvar('self.state', self.connect_button_state)
        # grid part: search for com port
        self.com_list_om.grid(column=0, row=0, sticky=tk.E + tk.W)
        combutton.grid(column=1, row=0, sticky=tk.E + tk.W)
        com_msg.grid(column=0, row=1, sticky=tk.W, columnspan=2)
        # grid part: setting port parameter
        lable_baudrate.grid(column=0, row=2)
        entry_baudrate.grid(column=1, row=2)
        lable_timeout.grid(column=0, row=3)
        entry_timeout.grid(column=1, row=3)
        # grid part: connect button and information
        self.connect_button.grid(column=0, row=4, sticky=tk.W + tk.S + tk.N + tk.E)
        self.time_view(connection_frame).grid(column=0, row=5, sticky=tk.W + tk.S + tk.N + tk.E, columnspan=2)
        return connection_frame

    def time_view(self,
                  parent,
                  ):
        self.time = time.asctime(time.localtime(time.time()))
        self.timevariable = tk.StringVar()
        self.timevariable.set(self.time)
        time_label = tk.Label(parent, textvariable=self.timevariable)
        return time_label

    def connect_button_event(self, widget=None
                             ):
        self.time = time.asctime(time.localtime(time.time()))
        self.timevariable.set(self.time)
        self.port.baudrate = self.entry_variable_baudrate.get()
        self.port.timeout = self.entry_variable_timeout.get()
        index = 0
        # TODO: find self.com_op in port list
        """
        try:
            index = self.get_com.portlist.index(self.com_op.get())
        except ValueError:
            print('Value Error!')
        """
        self.port.port = self.get_com.portlist[index].device
        # self.port.connect_to_port()
        try:
            if self.connect_text_variable.get() == 'Open':
                self.port.connect_to_port()
                if self.port.connect_state is True:
                    self.connect_text_variable.set('Close')
                else:
                    self.timevariable.set(self.time + '\n Timeout! Retry!')
            elif self.connect_text_variable.get() == 'Close':
                self.port.disconnect_port()
                self.connect_text_variable.set('Open')
        except IOError:
            print('IOError')
        except:
            print("Error!")

    def get_COM(self):
        self.get_com.get_serial_port()
        if self.get_com.port_state is False:
            self.com_state_msg.set('Port Unavailable!')
            self.connect_button.configure(state=tk.DISABLED)
        else:
            # text = 'Done!'
            self.com_state_msg.set(len(self.get_com.portlist))
            self.connect_button.configure(state=tk.ACTIVE)
            self.com_op.set(self.get_com.portlist[0])
            # self.com_list_om.configure(value=self.get_com.portlist[0])
            # self.com_list_om.configure(values=self.get_com.portlist)
