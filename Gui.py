import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
QLabel, QWidget, QPushButton, QLineEdit)
from PyQt6.QtGui import QFont
import pyqtgraph as pg
import random
import time
import threading

from PyQt6 import QtCore, QtGui, QtWidgets


class UI_MainWindow(object):
    def setupUI(self, Mainwindow):
        
        Mainwindow.setObjectName("Random Data Generator")
        self.setWindowTitle("Random Data Generator")
        self.is_generating = False
        self.gen_thread = None

        #create Main layouts
        self.layout1 = QVBoxLayout()
        self.layout2 = QVBoxLayout()
        self.layout3 = QVBoxLayout()
        self.layout4 = QVBoxLayout()
        self.layout5 = QHBoxLayout()
        self.layout6 = QHBoxLayout()
        self.layout7 = QHBoxLayout()
        self.layout8 = QHBoxLayout()

        #create widgets for layout
        self.label = QLabel("Game List Programm")
        self.label.setFont(QFont("Ink Free", 20))
        # font = label.font()
        # font.setBold(True)
        # font.setStyleName
        # label.setFont(font)
        # labelf.setPointSize(30)
        
        self.graphWidget = pg.PlotWidget()
        self.start_button = QPushButton("Start")
        #self.start_button.clicked.connect(self.start_generation)
        self.stop_button = QPushButton("Stop")
        #self.stop_button.clicked.connect(self.stop_generation)
        self.logdata_button = QPushButton("LogData")
        self.savedata_button = QPushButton("SaveData")
        
        #add widgets to layout
        self.layout4.addWidget(self.graphWidget)
        self.layout5.addWidget(self.start_button)
        self.layout6.addWidget(self.stop_button)
        self.layout7.addWidget(self.logdata_button)
        self.layout8.addWidget(self.savedata_button)

        
        #add sublayouts to mainlayout
        self.layout1.addLayout(self.layout2)
        self.layout1.addLayout(self.layout3)
        self.layout2.addLayout(self.layout4)
        self.layout3.addLayout(self.layout5)
        self.layout3.addLayout(self.layout6)
        self.layout3.addLayout(self.layout7)
        self.layout3.addLayout(self.layout8)
        
        self.widget = QWidget()
        self.widget.setLayout(self.layout1)
        self.setCentralWidget(self.widget)

    """def gen_data(self):                #https://www.influxdata.com/blog/how-convert-timestamp-to-datetime-in-python/
        print("Hallo")
         
        x_data = []
        y_data = []       
         
        start_time = time.time()
        actual_time = 0
        while self.is_generating and actual_time < 15:
            x_number = random.randint(1, 100)
            x_data.append(x_number)
            end_time = time.time()
            actual_time = end_time - start_time
            y_data.append(actual_time)
            print(x_data[-1], y_data[-1])
            time.sleep(5) 
    
        print(x_data, y_data)
    
    def start_generation(self):
        self.is_generating = True
        self.gen_thread = threading.Thread(target=self.gen_data)
        self.gen_thread.start()

    def stop_generation(self):
        if self.is_generating:
            self.is_generating = False
            if self.gen_thread:
                self.gen_thread.join(timeout=0.1)
                if self.gen_thread.is_alive():
                    print("Forcing thread termination")
                    self.gen_thread._stop()"""
            


