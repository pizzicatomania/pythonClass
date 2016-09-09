import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

class MyDlg:
    def __init__(self):
        self.ui = uic.loadUi('b.ui')
        self.ui.pushButton.clicked.connect(self.btn_click)
        self.ui.show()
    def btn_click(self):
        name = self.ui.lineEditName.text()
        age = self.ui.spinBoxAge.value()
        result = "이름: %s     나이: %d"%(name, age)
        self.ui.textEditResult.setText(result)

def main():
    app=QApplication(sys.argv)
    dlg = MyDlg()
    
    app.exec()


if __name__=='__main__':
    main()

print('closed')