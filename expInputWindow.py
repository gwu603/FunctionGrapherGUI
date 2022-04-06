from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5 import uic
from plotting import CanvasCreator
from functools import partial
import logging
import sys

class Exponential_UI(QMainWindow):
    def __init__(self):
        super(Exponential_UI,self).__init__()
        uic.loadUi("expinput.ui", self)
        self.createLocalVar()
        self.createGraphButton = self.findChild(QPushButton, "createGraph")
        self.createGraphButton.clicked.connect(self.showGraph)
        self.show()
        logging.info("opened exponential ui")

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
        logging.info("opening exponential graph ...")
        self.ui = CanvasCreator()
        self.ui.createExponentialCanvas(self.getInputData())
        self.clearAllText()

    def closeEvent(self, event):
        logging.info("closing exponential ui")
        event.accept()