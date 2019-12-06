from analize import Analize
from calculator import Calculator
import numpy as np

def main():
    analize = Analize()
    analize.analizis()
    newdata = analize.data
    first_col = [x[1] for x in newdata]
    second_col = [x[2] for x in newdata]
    third_col =  [x[3] for x in newdata]
    arr = []
    arr.append(first_col)
    arr.append(second_col)
    arr.append(third_col)
    print (np.asarray(arr))
    # Calculator.calc_correlation_matrix(np.asarray(arr))
    print(Calculator.calc_correlation_matrix(np.asarray(arr)))

if __name__ == "__main__":
    main()
