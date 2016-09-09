import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
class MyDlg:
    def __init__(self):
        self.ui = uic.loadUi("e.ui")
        self.ui.actionView1.triggered.connect(self.onview1)
        self.ui.actionView2.triggered.connect(self.onview2)        
        self.ui.show()
    def onview1(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def onview2(self):
        self.ui.stackedWidget.setCurrentIndex(1)

def main():
    app = QApplication(sys.argv)
    dlg = MyDlg()
    app.exec() 
if __name__ == '__main__':
    main()
    
    
    
    
    
    