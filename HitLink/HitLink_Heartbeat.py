# -*- coding:utf-8 -*-
# this is the hitlink module.

from HitLink import HitLink
from HitLink import protocol
import time


class HitLinkHeartbeat(HitLink):

    def __init__(self):
        self.hitlink_heartbeat_t = {'timestamp': 0x0000000000,
                                    'type': 0,
                                    'connect_flag': 0,
                                    'system_state': 0,
                                    }

    @classmethod
    def hitlink_payload2data(cls, payload, hitlink_heartbeat_data):
        temp = 0
        for i in range(4):
            temp <<= 8
            temp |= payload[i]
        hitlink_heartbeat_data['time_stamp'] = protocol.Transmit.bin2int(temp)
        temp = 0
        for i in range(4):
            temp <<= 8
            temp |= payload[4 + i]
        hitlink_heartbeat_data['type']= protocol.Transmit.bin2int(temp)
        temp = 0
        for i in range(4):
            temp <<= 8
            temp |= payload[8 + i]
        hitlink_heartbeat_data['connect_flag'] = protocol.Transmit.bin2int(temp)
        temp = 0
        for i in range(4):
            temp <<= 8
            temp |= payload[12 + i]
        hitlink_heartbeat_data['system_state'] = protocol.Transmit.bin2int(temp)

        return hitlink_heartbeat_data
