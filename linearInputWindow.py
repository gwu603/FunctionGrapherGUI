from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5 import uic
from plotting import CanvasCreator
from functools import partial
import sys

class Linear_UI(QMainWindow):
    def __init__(self):
        super(Linear_UI,self).__init__()
        uic.loadUi("linearInput.ui", self)
        self.createLocalVar()
        self.createParamGraphButton = self.findChild(QPushButton, "createParamGraph")
        self.createPointGraphButton = self.findChild(QPushButton, "createPointGraph")
        self.createParamGraphButton.clicked.connect(partial(self.openGraph, "param"))
        self.createPointGraphButton.clicked.connect(partial(self.openGraph, "point"))
        self.show()

    def createLocalVar(self):
        self.allInputs = {}
        self.allInputs["yint"] = self.findChild(QLineEdit, "yintInput")
        self.allInputs["slope"] = self.findChild(QLineEdit, "slopeInput")
        self.allInputs["x1"] = self.findChild(QLineEdit, "x1Input")
        self.allInputs["y1"] = self.findChild(QLineEdit, "y1Input")
        self.allInputs["x2"] = self.findChild(QLineEdit, "x2Input")
        self.allInputs["y2"] = self.findChild(QLineEdit, "y2Input")

    def clearAllText(self):
        for key in self.allInputs:
            self.allInputs[key].setText("")

    def getInputData(self):
        data = {}
        for key in self.allInputs:
            try:
                data[key] = float(self.allInputs[key].text())
            except:
                pass
        return data

    def openGraph(self, type):
        self.ui = CanvasCreator()
        self.ui.createLinearCanvas(type, self.getInputData())
        self.clearAllText()
    