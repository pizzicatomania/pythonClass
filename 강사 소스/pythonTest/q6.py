import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
class InDlg:
    def __init__(self, txt):
        self.ui = uic.loadUi("indlg.ui")
        self.ui.pushButton.clicked.connect(self.onDlgEnd)
        self.ui.lineEditDlg.setText(txt)
        self.ui.exec()# modal...
    def onDlgEnd(self):
        self.myTxt = self.ui.lineEditDlg.text()
        self.ui.close()
class MyDlg:
    def __init__(self):
        self.ui = uic.loadUi("d.ui") #xml ==>객체화
        self.ui.actionMy.triggered.connect(self.btn_click)
        self.ui.show()
    def btn_click(self):
        dlg = InDlg( self.ui.lineEditMain.text() )
        self.ui.lineEditMain.setText( dlg.myTxt )
        print("end..")
def main():
    app = QApplication(sys.argv)
    dlg = MyDlg()
    app.exec() #loop queue memory... 
if __name__ == '__main__':
    main()
    
    
    
    
  
  
  
    