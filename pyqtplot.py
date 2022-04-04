from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import uic
from linearInputWindow import Linear_UI
from expInputWindow import Exponential_UI
from polyInputWindow import Polynomial_UI
from functools import partial
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        uic.loadUi("functionSelect.ui", self)
        
        self.linearButton = self.findChild(QPushButton, "linearButton")
        self.linearButton.clicked.connect(self.openLinearInputWindow)
        self.expButton = self.findChild(QPushButton, "expButton")
        self.expButton.clicked.connect(self.openExpInputWindow)
        self.polyButton = self.findChild(QPushButton, "polyButton")
        self.polyButton.clicked.connect(self.openPolyInputWindow)
    
    def openLinearInputWindow(self):
        self.ui = Linear_UI()
    def openExpInputWindow(self):
        self.ui = Exponential_UI()
    def openPolyInputWindow(self):
        self.ui = Polynomial_UI()

def main():
    pyplot = QApplication(sys.argv)
    view = UI()
    view.show()
    sys.exit(pyplot.exec_())

if __name__ == '__main__':
	main()