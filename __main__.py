import numpy as np

from data_structure import DataStructure

data = np.loadtxt('./data/ecoli.txt', dtype={'names': (
    'sequenceName', 'mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2', 'localization'),
    'formats': (
        'U20', np.float, np.float, np.float, np.float, np.float, np.float, np.float, "U3"
)})

dataStructure = DataStructure(data['sequenceName'], data['mcg'], data['gvh'], data['lip'],
                              data['chg'], data['aac'], data['alm1'], data['alm2'], data['localization'])

print(dataStructure.gvh)
print(DataStructure.calc_arithmetic_mean(dataStructure.gvh))
print(DataStructure.calc_median(dataStructure.gvh))
print(DataStructure.calc_minimum(dataStructure.gvh))
print(DataStructure.calc_maximum(dataStructure.gvh))