import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

class MyDlg:
    def __init__(self):
        self.ui = uic.loadUi('num.ui')
        self.ui.pushButton.clicked.connect(self.btn_click)
        self.ui.show()
    def btn_click(self):
        num1 = int(self.ui.lineEditNum1.text())
        num2 = int(self.ui.lineEditNum2.text())
        
        result ="%d"%(num1+num2)
        self.ui.textEditResult.setText(result)

def main():
    app=QApplication(sys.argv)
    dlg = MyDlg()
    
    app.exec()


if __name__=='__main__':
    main()

print('closed')