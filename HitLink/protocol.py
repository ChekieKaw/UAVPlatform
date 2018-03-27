from HitLink import HitLink
import os, sys
import math


class Transmit:
    @classmethod
    def bin2int(cls, bin_num):
        return int(bin_num)

    @classmethod
    def bin2float(cls, bin_num):
        if (bin_num >> 31) == 1:
            flag = 1
        else:
            flag = (-1)
        # flag = (-1) * (bin_num >> 31)
        ex = int((bin_num >> 23) & 0xFF)
        # Mx_temp = (bin_num << 9) >> 9
        mx = float(0.0)
        for i in range(23):
            mx += ((bin_num >> (22 - i)) & 0b1) * math.pow(0.5, (i + 1))
        return flag * (ex + mx)
