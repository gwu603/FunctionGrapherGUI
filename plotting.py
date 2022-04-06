import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
import logging

class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=50)
        super().__init__(self.fig)
        self.setParent(parent)
        self.x = np.linspace(-5,5,100)

    def plotLinearGraph(self, yint, slope):
        y = slope*self.x+yint
        funcName = f'y={slope}x+{yint}'
        self.updateGraphLabel(y, funcName)

    def plotExpGraph(self, A, B):
        y = np.power(A,self.x) + B
        funcName = f'y={A}^x+{B}'
        self.updateGraphLabel(y, funcName)

    def plotPolyGraph(self, A, B):
        y = np.power(self.x,A) + B
        funcName = f'y=x^{A}+{B}'
        self.updateGraphLabel(y, funcName)
        
    def updateGraphLabel(self, y, funcName):
        self.ax.plot(self.x,y, "-r", label=funcName)
        self.ax.set(xlabel='x', ylabel='y', title=funcName)
        self.ax.grid()
        self.fig.savefig(f'{funcName}.png')

class CanvasCreator(QWidget):
    def createLinearCanvas(self, type, data):
        self.chart = Canvas(self)
        if type == "param":
            self.chart.plotLinearGraph(data["yint"], data["slope"])
        else:
            yint, slope = self.calcLinearFunction(data)
            self.chart.plotLinearGraph(yint, slope)
        self.show()
        logging.info("opened linear graph")
    
    def calcLinearFunction(self, data):
        slope = (data["y2"] - data["y1"]) / (data["x2"] - data["x1"])
        yint = data["y1"] - slope*data["x1"]
        return yint, slope
    
    def createExponentialCanvas(self, data):
        self.chart = Canvas(self)
        self.chart.plotExpGraph(data["A"], data["B"])
        self.show()
        logging.info("opened exponential graph")

    def createPolynomialCanvas(self, data):
        self.chart = Canvas(self)
        self.chart.plotPolyGraph(data["A"], data["B"])
        self.show()
        logging.info("opened polynomial graph")

