from PyQt6.QtWidgets import QMainWindow, QApplication
import sys, time, random, threading
from Gui import UI_MainWindow
from functions import Functions
from PyQt6.QtCore import QTimer, Qt

class DataGenWindow(QMainWindow): #UI_MainWindow
        def __init__(self):
                super().__init__()                      #setupUI als Übermethode initialisiert
                self.ui = UI_MainWindow()
                self.ui.setupUI(self)
                self.main_API = Functions()
                self.connect_buttons()
                self.show()

        def connect_buttons(self):
                #self.functions = Functions()                                            #Wie wenn ich Klasse Student anlege
                self.ui.start_button.clicked.connect(self.main_API.start_generation)
                self.ui.logdata_button.clicked.connect(self.main_API.update_graph)        #überinitialisierte Methoden abrufen
                self.ui.stop_button.clicked.connect(self.main_API.stop_generation) 

        def update_graph(self):
                x_data, y_data = self.functions.get_data()
                self.ui.graphWidget.clear()
                self.ui.graphWidget.plot(x_data, y_data)

        # def update_graph(self):
        #         if self.start_button == True:
                       # self.graphWidget.plot(self.x_data, self.y_data)
                
                
                     

        

app = QApplication(sys.argv)
DataGen = DataGenWindow()
app.exec()
