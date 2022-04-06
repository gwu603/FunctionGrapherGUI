from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog, QPlainTextEdit
from PyQt5 import uic
from linearInputWindow import Linear_UI
from expInputWindow import Exponential_UI
from polyInputWindow import Polynomial_UI
from functools import partial
import logging
from PIL import Image        
import sys

class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        # self.widget = QPlainTextEdit(parent)
        # self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("functionSelect.ui", self)
        self.createLogger()
        logging.info("opened function select ui")
        self.linearButton = self.findChild(QPushButton, "linearButton")
        self.linearButton.clicked.connect(self.openLinearInputWindow)
        self.expButton = self.findChild(QPushButton, "expButton")
        self.expButton.clicked.connect(self.openExpInputWindow)
        self.polyButton = self.findChild(QPushButton, "polyButton")
        self.polyButton.clicked.connect(self.openPolyInputWindow)
        self.openGraphButton = self.findChild(QPushButton, "openGraphButton")
        self.openGraphButton.clicked.connect(self.openGraph)

    def createLogger(self):
        self.logBox = self.findChild(QPlainTextEdit, "logger")
        self.logBox.setReadOnly(True)
        self.logTextBox = QTextEditLogger(self)
        self.logTextBox.widget = self.logBox
        self.logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(self.logTextBox)
        logging.getLogger().setLevel(logging.INFO)
    
    def openLinearInputWindow(self):
        logging.info("opening linear input ui ...")
        self.ui = Linear_UI()
    def openExpInputWindow(self):
        logging.info("opening exponential input ui ...")

        self.ui = Exponential_UI()
    def openPolyInputWindow(self):
        logging.info("opening polynomial input ui ...")
        self.ui = Polynomial_UI()
    def openGraph(self):
        logging.info("opening saved graph ...")
        fname = QFileDialog.getOpenFileName(self, "Open Graph", "", "PNG Files (*.png)")
        if fname:
            img = Image.open(fname[0])
            img.show()
            logging.info("opened saved graph")

def main():
    pyplot = QApplication(sys.argv)
    view = UI()
    view.show()
    sys.exit(pyplot.exec_())

if __name__ == '__main__':
	main()