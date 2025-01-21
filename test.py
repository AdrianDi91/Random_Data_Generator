import pytest
import main
from Gui import *

def Gen_Data_Test():
    x_data, y_data = main.Gen_Data()
    assert len(x_data) == 4
    assert len(y_data) == 4
    assert round(y_data[-1]) == 15

def test_Gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
#Gen_Data_Test()
test_Gui()
