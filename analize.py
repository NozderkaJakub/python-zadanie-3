import numpy as np
from collections import Counter

from calculator import Calculator
import matplotlib
import matplotlib.pyplot as plt

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
        for element in dataTypes[:7]:
            print('==' + element + '==')
            for function in quantitativeFunctions:
                function(self.data[element], verbose=True)
            print('\n')
        
        for element in dataTypes[7:]:
            print('==' + element + '==')
            Calculator.calc_mode(self.data[element], verbose=True)
            print('\n')

        matrix = self.get_correlation_array()
        self.histogram()
        self.draw_heatmap(matrix)
        self.draw_regression_curve()


    def draw_heatmap(self, matrix):
        fig, ax = plt.subplots()
        im, cbar = self.heatmap(matrix, ax=ax, cmap="YlGn", cbarlabel="")
        texts = self.annotate_heatmap(im, valfmt="{x:.5f}")
        fig.tight_layout()
        plt.show()

    
    def get_correlation_array(self):
        arr = []
        for i in range(7):
            arr.append( [x[i+1] for x in self.data] )
        matrix = Calculator.calc_correlation_matrix(np.asarray(arr))
        print('Macierz korelacji dla cech ilościowych')
        print(matrix)
        return matrix


    def draw_regression_curve(self):
        x = self.data['aac']
        y = self.data['alm2']
        coef = np.polyfit(x, y, 1)
        poly1d_fn = np.poly1d(coef) 
        plt.plot(x, y, 'yo', x, poly1d_fn(x), '--k')
        plt.plot()
        plt.show()



    def histogram(self):
        plt.hist(self.data['aac'], alpha=0.5, label='aac')
        plt.hist(self.data['alm2'], alpha=0.5, label='alm2')
        plt.legend(loc='upper right')
        plt.show()


    def heatmap(self, data, ax=None, cbar_kw={}, cbarlabel="", **kwargs):
        if not ax:
            ax = plt.gca()

        # Plot the heatmap
        im = ax.imshow(data, **kwargs)

        # Create colorbar
        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

        # We want to show all ticks...
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_yticks(np.arange(data.shape[0]))
        # ... and label them with the respective list entries.
        ax.set_xticklabels(dataTypes[0:7])
        ax.set_yticklabels(dataTypes[0:7])

        # Let the horizontal axes labeling appear on top.
        ax.tick_params(top=True, bottom=False,
                    labeltop=True, labelbottom=False)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
                rotation_mode="anchor")

        # Turn spines off and create white grid.
        for edge, spine in ax.spines.items():
            spine.set_visible(False)

        ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
        ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
        ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
        ax.tick_params(which="minor", bottom=False, left=False)

        return im, cbar


    def annotate_heatmap(self, im, data=None, valfmt="{x:.2f}", textcolors=["black", "white"], threshold=None, **textkw):

        if not isinstance(data, (list, np.ndarray)):
            data = im.get_array()

        # Normalize the threshold to the images color range.
        if threshold is not None:
            threshold = im.norm(threshold)
        else:
            threshold = im.norm(data.max())/2.

        # Set default alignment to center, but allow it to be
        # overwritten by textkw.
        kw = dict(horizontalalignment="center",
                verticalalignment="center")
        kw.update(textkw)

        # Get the formatter in case a string is supplied
        if isinstance(valfmt, str):
            valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

        # Loop over the data and create a `Text` for each "pixel".
        # Change the text's color depending on the data.
        texts = []
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
                text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
                texts.append(text)

        return texts