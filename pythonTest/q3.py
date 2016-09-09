import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

class MyDlg:
    def __init__(self):
        self.ui = uic.loadUi('a.ui')
        self.ui.show()
        self.ui.oneBtn.clicked.connect(self.btn_click)
        
    def btn_click(self):
        txt = self.ui.lineEdit.text()
        print(txt)
#         print('clicked')
#         self.ui.lineEdit.setText('ahhhhhhhhh')


def main():
    app=QApplication(sys.argv)
    dlg = MyDlg()
    
    app.exec()


if __name__=='__main__':
    main()

print('closed')