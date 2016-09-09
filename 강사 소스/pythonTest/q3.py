import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
class MyDlg:
    def __init__(self):
        self.ui = uic.loadUi("a.ui") #xml ==>객체화
        self.ui.oneBtn.clicked.connect( self.btn_click )
        self.ui.show()
    def btn_click(self):
        txt = self.ui.lineEdit.text()
        print(txt)
#         self.ui.lineEdit.setText('대한민국')
#         print('hello')
def main():
    app = QApplication(sys.argv)
    dlg = MyDlg()
    app.exec() #loop queue memory... 
if __name__ == '__main__':
    main()
    
    
    
    
    
    