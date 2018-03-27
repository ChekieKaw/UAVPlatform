# -*- coding:utf-8 -*-
# this is the connect control module, to ensure serial and heartbeat package available

import serial
import serial.tools.list_ports
import tkinter as tk
from Connect import ConnectView


# TODO: write an function class to read and write data via port


class ConnectControl():

    def __init__(self):
        self.portlist = ['Null']
        self.port_state = False
        self.baudrate = 9600
        self.port = None
        self.timeout = 0
        self.write_timeout = 0
        self.connect_state = False
        self.connect = serial.Serial(port=self.port,
                                     baudrate=self.baudrate,
                                     timeout=self.timeout,
                                     write_timeout=self.write_timeout,
                                     rtscts=True
                                     )

    def get_serial_port(self):
        # self.portlist = list(serial.tools.list_ports.comports())
        if len(list(serial.tools.list_ports.comports())) <= 0:
            self.port_state = False
            self.portlist = ['Null']
        else:
            self.portlist = list(serial.tools.list_ports.comports())
            self.port_state = True

    def event_port_state(self):
        pass

    def connect_to_port(self, widget=None):
        self.connect.baudrate = self.baudrate
        self.connect.port = self.port
        self.connect.timeout = self.timeout
        self.connect.write_timeout = self.write_timeout
        self.connect.rtscts = True

        try:
            self.connect.open()
        except serial.SerialTimeoutException:
            self.connect_state = False
            print('Timeout')
        else:
            self.connect_state = True

    # TODO: add Connect method (basing on protocol)

    def disconnect_port(self, widget=None):
        self.connect.close()
        self.connect_state = False
