import numpy as np

from data_structure import DataStructure

data = np.loadtxt('./data/ecoli.txt', dtype={'names': (
    'sequenceName', 'mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2', 'localization'),
    'formats': (
        'U20', np.float, np.float, np.float, np.float, np.float, np.float, np.float, "U3"
)})

print(data)