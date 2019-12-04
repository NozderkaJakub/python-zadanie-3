import numpy as np

from calculator import Calculator

quantitativeFunctions = [Calculator.calc_arithmetic_mean, Calculator.calc_standard_deviation, Calculator.calc_median,
                        Calculator.calc_minimum, Calculator.calc_maximum]


dataTypes = ['mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2', 'sequenceName', 'localization']

class Analize:

    def __init__(self):
        self.data = np.loadtxt('./data/ecoli.txt', dtype={'names': (
            'sequenceName', 'mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2', 'localization'),
            'formats': (
                'U20', np.float, np.float, np.float, np.float, np.float, np.float, np.float, "U3"
        )})


    def analizis(self):
        while(1):
            self.decide()


    def decide(self):
        decision = input('Podaj numer danych, na których chcesz operować\n' + 
                        '1) mcg\n' + '2) gvh\n' + '3) lip\n' + '4) chg\n' + '5) aac\n' +
                        '6) alm1\n' + '7) alm2\n' + '8) sequenceName\n' + '9) localization\n' + 'wybór: ')
        if decision in ['1', '2', '3', '4', '5', '6', '7']:
            self.quantitativeCharacteristic(decision)
        elif decision in ['8', '9']:
            self.qualityCharacteristic(decision)
        else:
            print('Nie ma takich danych...')

            
    def quantitativeCharacteristic(self, decision):
        operation = input('Jaką operację chcesz wykonać?\n' + '   1) średnia arytmetyczna\n' + '   2) odchylenie standardowe\n' +
                        '   3) mediana\n' + '   4) minimum\n' + '   5) maximum\n' + '   wynór: ')
        quantitativeFunctions[int(operation) - 1](self.data[dataTypes[int(decision) - 1]], verbose=True)


    def qualityCharacteristic(self, decision):
        Calculator.calc_mode(self.data[dataTypes[int(decision) - 1]], verbose=True)
