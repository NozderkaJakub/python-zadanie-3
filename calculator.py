import collections
import math
import numpy as np
import pandas as pd
import seaborn as sns
from data import Data

d = Data()
sequenceName = d.data['sequenceName']
localization = d.data['localization']

class Calculator:

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
    def dominant(cls):
        data = []
        data.append(list(cls.calc_mode(sequenceName)))
        data.append(list(cls.calc_mode(localization)))
        print(pd.DataFrame(data, columns=["Dominanta", "Liczebność", "Częstość"]))

    @classmethod
    def calc_arithmetic_mean(cls, data):
        return np.sum(data) / len(data)

    @classmethod
    def calc_standard_deviation(cls, data):
        arithmetic_mean = Calculator.calc_arithmetic_mean(data)
        differences = data - arithmetic_mean
        powers = differences ** 2
        sums = sum(powers)
        variance = sums / len(data)
        standard_deviation = math.sqrt(variance)
        return standard_deviation

    @classmethod
    def calc_median(cls, data):
        N = len(data)
        data = np.sort(data)
        return (data[(N//2)-1] + data[N//2]) / 2 if N % 2 == 0 else data[(N-1)//2]

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
        return value, number, number / len(data)

    @classmethod
    def calc_correlation_matrix(cls, data, dataframe=False):
        columns_no = len(data)
        correlations = np.zeros(shape=(columns_no, columns_no))
        # print(data.items())
        keys = [k for (k, _) in data.items()]
        for i in enumerate(keys):
            for j in enumerate(keys):
                correlations[i[0]][j[0]] = Calculator.calc_correlation(
                    np.asarray([data[i[1]], data[j[1]]])
                )
        return Calculator.__as_dataframe(correlations, keys) if dataframe else correlations

    @classmethod
    def calc_correlation(cls, data):
        covariance = Calculator.calc_covariance(data)
        X_std_deviation = Calculator.calc_standard_deviation(
            np.asarray(data[0]))
        Y_std_deviation = Calculator.calc_standard_deviation(
            np.asarray(data[1]))
        return covariance / (X_std_deviation*Y_std_deviation)

    @classmethod
    def calc_covariance(cls, data):
        EX = Calculator.calc_arithmetic_mean(data[0])
        EY = Calculator.calc_arithmetic_mean(data[1])
        EXY = Calculator.calc_arithmetic_mean(data[0]*data[1])
        covariance = EXY - (EX*EY)
        return covariance


    @classmethod
    def __as_dataframe(cls, data, keys):
        tmp = {}
        for i in range(0, len(data)):
            tmp[keys[i]] = [x[i] for x in data]
        return pd.DataFrame(tmp, columns=keys, index=keys)