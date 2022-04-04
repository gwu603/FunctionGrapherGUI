import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget

class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=50)
        super().__init__(fig)
        self.setParent(parent)

    def plotLinearGraph(self, yint, slope):
        x = np.linspace(-5,5,100)
        y = slope*x+yint
        self.ax.plot(x,y, "-r", label='y=2x+1')
        self.ax.set(xlabel='x', ylabel='y',
               title=f'y={slope}x+{yint}')
        self.ax.grid()

    def plotExpGraph(self, A, B):
        x = np.linspace(-5,5,100)
        y = np.power(A,x) + B
        self.ax.plot(x,y, "-r", label=f'y={A}^x+{B}')
        self.ax.set(xlabel='x', ylabel='y',
               title=f'y={A}^x+{B}')
        self.ax.grid()
    
    def plotPolyGraph(self, A, B):
        x = np.linspace(-5,5,100)
        y = np.power(x,A) + B
        self.ax.plot(x,y, "-r", label=f'y=x^{A}+{B}')
        self.ax.set(xlabel='x', ylabel='y',
               title=f'y=x^{A}+{B}')
        self.ax.grid()

class CanvasCreator(QWidget):
    def createLinearCanvas(self, type, data):
        self.chart = Canvas(self)
        if type == "param":
            self.chart.plotLinearGraph(data["yint"], data["slope"])
        else:
            yint, slope = self.calcLinearFunction(data)
            self.chart.plotLinearGraph(yint, slope)
        self.show()
    
    def calcLinearFunction(self, data):
        slope = (data["y2"] - data["y1"]) / (data["x2"] - data["x1"])
        yint = data["y1"] - slope*data["x1"]
        return yint, slope
    
    def createExponentialCanvas(self, data):
        self.chart = Canvas(self)
        self.chart.plotExpGraph(data["A"], data["B"])
        self.show()

    def createPolynomialCanvas(self, data):
        self.chart = Canvas(self)
        self.chart.plotPolyGraph(data["A"], data["B"])
        self.show()
