from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5 import uic
from plotting import CanvasCreator
from functools import partial
import logging
import sys

class Polynomial_UI(QMainWindow):
    def __init__(self):
        super(Polynomial_UI,self).__init__()
        uic.loadUi("polyinput.ui", self)
        self.createLocalVar()
        self.createGraphButton = self.findChild(QPushButton, "createGraph")
        self.createGraphButton.clicked.connect(self.showGraph)
        self.show()
        logging.info("opened polynomial ui")

    def createLocalVar(self):
        self.allInputs = {}
        self.allInputs["A"] = self.findChild(QLineEdit, "aInput")
        self.allInputs["B"] = self.findChild(QLineEdit, "bInput")
        
    def getInputData(self):
        data = {}
        data["A"] = float(self.allInputs["A"].text())
        data["B"] = float(self.allInputs["B"].text())
        return data

    def clearAllText(self):
        for key in self.allInputs:
            self.allInputs[key].setText("")

    def showGraph(self):
        logging.info("opening polynomial graph ...")
        self.ui = CanvasCreator()
        self.ui.createPolynomialCanvas(self.getInputData())
        self.clearAllText()
    
    def closeEvent(self, event):
        logging.info("closing polynomial ui")
        event.accept()