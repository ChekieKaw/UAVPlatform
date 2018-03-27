# -*- coding:utf-8 -*-

import tkinter as tk
import math


class Angle:
    deg = 0.0
    rad = 0.0

    def __init__(self):
        if self.deg == 0 or self.rad == 0:
            if self.deg == 0 and self.rad != 0:
                self.deg = self.rad2deg()
            elif self.rad == 0 and self.deg != 0:
                self.rad = self.deg2rad()

    def deg2rad(self):
        self.rad = self.deg / 180 * math.pi
        return self.rad

    def rad2deg(self):
        self.deg = self.rad / math.pi * 180
        return self.deg


class PostureData(Angle):
    row = Angle()
    pitch = Angle()
    yaw = Angle()


class FlightData:
    altitude = 0.0
    ground_velocity = 0.0
    air_velocity = 0.0
    distant_home = 0.0


class DataView:

    def __init__(self):
        self.posture = PostureData()
        self.flight = FlightData()
        self.mode = ('deg', 'rad')

    def posture_view(self,
                     parent=None,
                     angle_mode='deg'
                     ):
        posture_frame = tk.LabelFrame(parent, text='Posture')
        text_row = tk.Label(posture_frame, text='Row')
        text_pitch = tk.Label(posture_frame, text='Pitch')
        text_yaw = tk.Label(posture_frame, text='Yaw')
        row = tk.DoubleVar()
        pitch = tk.DoubleVar()
        yaw = tk.DoubleVar()
        if angle_mode == 'deg':
            row.set(self.posture.row.deg)
            pitch.set(self.posture.pitch.deg)
            yaw.set(self.posture.yaw.deg)
            # row = self.posture.row.deg
            # pitch = self.posture.pitch.deg
            # yaw = self.posture.yaw.deg

        elif angle_mode == 'rad':
            row.set(self.posture.row.rad)
            pitch.set(self.posture.pitch.rad)
            yaw.set(self.posture.yaw.rad)
        else:
            return 0
        data_row = tk.Label(posture_frame, textvariable=row)
        data_pitch = tk.Label(posture_frame, textvariable=pitch)
        data_yaw = tk.Label(posture_frame, textvariable=yaw)
        # gird part
        posture_frame.columnconfigure(0, weight=1)

        text_row.grid(column=0, row=0, sticky=tk.W)
        text_pitch.grid(column=0, row=1, sticky=tk.W)
        text_yaw.grid(column=0, row=2, sticky=tk.W)
        data_row.grid(column=1, row=0, columnspan=2, sticky=tk.E)
        data_pitch.grid(column=1, row=1, columnspan=2, sticky=tk.E)
        data_yaw.grid(column=1, row=2, columnspan=2, sticky=tk.E)
        return posture_frame

    def flightdata_view(self, parent=None):
        altitude = tk.DoubleVar()
        ground_velocity = tk.DoubleVar()
        air_velocity = tk.DoubleVar()
        distant_home = tk.DoubleVar()
        altitude.set(0.0)
        ground_velocity.set(0.0)
        air_velocity.set(0.0)
        distant_home.set(0.0)
        flight_frame = tk.LabelFrame(parent, text='Flight Data')
        text_altitude = tk.Label(flight_frame, text='Altitude')
        text_ground = tk.Label(flight_frame, text='Ground Velocity')
        text_air = tk.Label(flight_frame, text='Air Velocity')
        text_distant = tk.Label(flight_frame, text='Distant to HOME')
        data_altitude = tk.Label(flight_frame, textvariable=altitude)
        data_ground = tk.Label(flight_frame, textvariable=ground_velocity)
        data_air = tk.Label(flight_frame, textvariable=air_velocity)
        data_distant = tk.Label(flight_frame, textvariable=distant_home)
        # grid
        flight_frame.columnconfigure(0, weight=1)
        text_altitude.grid(column=0, row=0, sticky=tk.W)
        text_ground.grid(column=0, row=1, sticky=tk.W)
        text_air.grid(column=0, row=2, sticky=tk.W)
        text_distant.grid(column=0, row=3, sticky=tk.W)
        data_altitude.grid(column=1, row=0, columnspan=2, sticky=tk.E)
        data_ground.grid(column=1, row=1, columnspan=2, sticky=tk.E)
        data_air.grid(column=1, row=2, columnspan=2, sticky=tk.E)
        data_distant.grid(column=1, row=3, columnspan=2, sticky=tk.E)
        # flight_frame.mainloop()
        return flight_frame
