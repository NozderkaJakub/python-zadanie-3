import numpy as np


class Data:
    def __init__(self):
        data = self.__load_txt()
        self.data = self.__as_dict(data)

    def __as_dict(self, data):
        def get_column(index):
            return [x[index] for x in data]

        columns = ['sequenceName', 'mcg', 'gvh', 'lip',
                   'chg', 'aac', 'alm1', 'alm2', 'localization']
        columns_no = len(columns)
        newdata = {}
        for index in range(0, columns_no):
            newdata[columns[index]] = get_column(index)
        return newdata

    def __load_txt(self):
        return np.loadtxt(
            './data/ecoli.txt',
            dtype={
                'names': (
                    'sequenceName', 'mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2', 'localization'),
                'formats': (
                    'U20', np.float, np.float, np.float, np.float, np.float, np.float, np.float, "U3"
                )
            }
        )

    def get_subdata_by_columns(self, keys):
        return {key: self.data[key] for key in keys}