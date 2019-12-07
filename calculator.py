import collections
import math
import numpy as np


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
    def calc_arithmetic_mean(cls, data, verbose=False):
        arithmetinc_mean = np.sum(data)/len(data)
        if verbose:
            print('Średnia arytmetyczna jest równa ' + str(arithmetinc_mean))
        return arithmetinc_mean

    @classmethod
    def calc_standard_deviation(cls, data, verbose=False):
        arithmetic_mean = Calculator.calc_arithmetic_mean(data)
        differences = data - arithmetic_mean
        powers = differences**2
        sums = sum(powers)
        variance = sums/len(data)
        standard_deviation = math.sqrt(variance)
        if verbose:
            print('Odchylenie standardowe jest równe ' + str(standard_deviation))
        return standard_deviation

    @classmethod
    def calc_median(cls, data, verbose=False):
        length = len(data)
        data = np.sort(data)
        median = data[(
            length-1)//2] if length % 2 != 0 else (data[(length//2)-1] + data[length//2]) / 2
        if verbose:
            print('Mediana jest równa ' + str(median))
        return median

    @classmethod
    def calc_minimum(cls, data, verbose=False):
        minimum = min(data)
        if verbose:
            print('Minimum jest równe ' + str(minimum))
        return minimum

    @classmethod
    def calc_maximum(cls, data, verbose=False):
        maximum = max(data)
        if verbose:
            print('Maximum jest równe ' + str(maximum))
        return maximum

    @classmethod
    def calc_mode(cls, data, verbose=False):
        value, number = max(
            collections.Counter(data).items(),
            key=lambda x: x[1]
        )
        (value, number, rate) = value, number, number / len(data)
        if verbose:
            print('Dominanta to \"' + str(value) + '\" a jej liczebność to ' +
                  str(number) + ' przy częstości ' + str(rate))
        return (value, number, rate)

    @classmethod
    def calc_correlation_matrix(cls, data):
        columns_no = len([x[0] for x in data])
        # print(columns_no)
        correlations = np.zeros(shape=(columns_no, columns_no))
        for i in range(0, columns_no):
            for j in range(0, columns_no):
                X = [x[i] for x in data]
                Y = [x[j] for x in data]
                _data = np.array([X, Y])
                covariance = Calculator.calc_covariance(np.asarray(_data))
                X_std_derivation = Calculator.calc_standard_deviation(
                    np.asarray(X))
                Y_std_derivation = Calculator.calc_standard_deviation(
                    np.asarray(Y))
                correlation = covariance / (X_std_derivation*Y_std_derivation)
                correlations[i][j] = correlation
        return correlations

    @classmethod
    def calc_covariance(cls, data):
        X = data[0]
        Y = data[1]
        EX = Calculator.calc_arithmetic_mean(X)
        EY = Calculator.calc_arithmetic_mean(Y)
        EXY = Calculator.calc_arithmetic_mean(X*Y)
        covariance = EXY - (EX*EY)
        return covariance

    @classmethod
    def calc_correlation(cls, data):
        pass
