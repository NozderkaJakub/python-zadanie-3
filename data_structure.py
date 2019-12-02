import collections
import math
import numpy as np


class DataStructure:

    def __init__(self, sequenceName, mcg, gvh, lip, chg, aac, alm1, alm2, localization):
        self.sequenceName = sequenceName
        self.mcg = mcg
        self.gvh = gvh
        self.lip = lip
        self.chg = chg
        self.aac = aac
        self.alm1 = alm1
        self.alm2 = alm2
        self.localization = localization

    @classmethod
    def calc_arithmetic_mean(cls, data):
        return np.sum(data)/len(data)

    @classmethod
    def calc_standard_deviation(cls, data):
        pass

    @classmethod
    def calc_median(cls, data):
        length = len(data)
        data = np.sort(data)
        return data[(length-1)//2] if length % 2 != 0 else (data[(length//2)-1] + data[length//2]) / 2

    @classmethod
    def calc_minimum(cls, data):
        return min(data)

    @classmethod
    def calc_maximum(cls, data):
        return max(data)

    @classmethod
    def calc_mode(cls, data):
        value, number = max(
            collections.Counter(data).items(),
            key=lambda x: x[1]
        )
        (value, number, rate) = value, number, number / len(data)
        return (value, number, rate)
