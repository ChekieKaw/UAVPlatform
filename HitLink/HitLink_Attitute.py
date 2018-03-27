# -*- coding:utf-8 -*-
# this is the connect control module, to ensure serial and heartbeat package available
from HitLink import HitLink
from HitLink import protocol


class HitLinkAttitute(HitLink):

    def __init__(self):
        self.hitlink_attitute_t = {'time_stamp': 0x00000000,
                                   'row': 0.0,
                                   'pitch': 0.0,
                                   'yaw': 0.0,
                                   'row_speed': 0.0,
                                   'yaw_speed': 0.0,
                                   'pitch_speed': 0.0
                                   }

    @classmethod
    def hitlink_payload2data(cls, payload, hitlink_attitute_data):
        temp = 0
        for i in range(4):
            temp <<= 8
            temp |= payload[i]
        hitlink_attitute_data['time_stamp'] = protocol.Transmit.bin2int(temp)
        temp = 0
        for i in range(4):
            temp <<= 8
            temp |= payload[i + 4]
        hitlink_attitute_data['row'] = protocol.Transmit.bin2float(temp)
        temp = 0
        for i in range(4):
            temp <<= 8
            temp |= payload[i + 8]
        hitlink_attitute_data['pitch'] = protocol.Transmit.bin2float(temp)
        temp = 0
        for i in range(4):
            temp <<= 8
            temp |= payload[i + 12]
        hitlink_attitute_data['yaw'] = protocol.Transmit.bin2float(temp)
        for i in range(4):
            temp <<= 8
            temp |= payload[i + 16]
        hitlink_attitute_data['row_speed'] = protocol.Transmit.bin2float(temp)
        temp = 0
        for i in range(4):
            temp <<= 8
            temp |= payload[i + 20]
        hitlink_attitute_data['pitch_speed'] = protocol.Transmit.bin2float(temp)
        temp = 0
        for i in range(4):
            temp <<= 8
            temp |= payload[i + 24]
        hitlink_attitute_data['yaw_speed'] = protocol.Transmit.bin2float(temp)
        temp = 0
        return hitlink_attitute_data
