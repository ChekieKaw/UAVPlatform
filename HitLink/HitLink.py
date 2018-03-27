# -*- coding:utf-8 -*-
# this is the connect control module, to ensure serial and heartbeat package available

from crccheck.crc import CrcX25
from HitLink import HitLink_Attitute
from HitLink import HitLink_Heartbeat



class HitLink:

    def __init__(self):
        self.hitlink_STR = 0xEF
        self.hitlink_max_len = 255
        self.hitlink_max_seq = 255
        self.hitlink_msg_dict = {'start': 0xEF,
                                 'sequence': 0,
                                 'payload_len': 0,
                                 'message': 0,
                                 'payload': [],
                                 'crc_h': 0xff,
                                 'crc_l': 0xff,
                                 'crc': 0xffff,
                                 'checkflag': False}
        self.crc = []
        self.crc_cal = 0xffff
        self.checkflag = False

    def hitlink_unpack_msg(self, buffer):
        """

        :param buffer:  byte array get from serial.
        :return: message dictionary (byte arrary)
        """
        if buffer[0] != 0xFE:
            return 0
        else:
            self.hitlink_msg_dict['start'] = buffer[0]
            self.hitlink_msg_dict['sequence'] = buffer[1]
            self.hitlink_msg_dict['payload_len'] = buffer[2]
            self.hitlink_msg_dict['message'] = buffer[3]
            self.hitlink_msg_dict['payload'] = buffer[4:(4 + self.hitlink_msg_dict['payload_len'])]
            self.hitlink_msg_dict['crc_h'] = buffer[(5 + self.hitlink_msg_dict['payload_len'])]
            self.hitlink_msg_dict['crc_l'] = buffer[(6 + self.hitlink_msg_dict['payload_len'])]
            self.crc_cal = CrcX25.calcbytes(buffer)
            self.crc.append(self.hitlink_msg_dict['crc_h'])
            self.crc.append(self.hitlink_msg_dict['crc_l'])
        if self.crc == self.crc_cal:
            self.checkflag = True
            return self.hitlink_msg_dict
        else:
            return 0

    @classmethod
    def hitlink_payload_unpack(cls,msg_dict):
        if msg_dict['message'] == 0:
            hitlink_heartbeat = HitLink_Heartbeat.HitLinkHeartbeat()
            hitlink_heartbeat.hitlink_payload2data(msg_dict['payload'],hitlink_heartbeat.hitlink_heartbeat_t)
