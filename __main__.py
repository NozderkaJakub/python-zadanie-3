from analyzer import Analize
from calculator import Calculator as Calc
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from data import Data

def main():
    data = Data()
    newdata = data.get_subdata_by_columns(['mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2'])

if __name__ == "__main__":
    main()