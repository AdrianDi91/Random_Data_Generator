from PyQt6.QtWidgets import QMainWindow, QApplication
import sys, time, random, threading
from Gui import UI_MainWindow
from functions import Functions

class DataGenWindow(QMainWindow, UI_MainWindow):
        def __init__(self):
                super().__init__()
                self.setupUI(self)
                self.show()
                
                self.functions = Functions()
                self.start_button.clicked.connect(self.functions.start_generation)
                self.stop_button.clicked.connect(self.functions.stop_generation)

                #self.logdata_button.clicked.connect(self.logger)

app = QApplication(sys.argv)
DataGen = DataGenWindow()
app.exec()
