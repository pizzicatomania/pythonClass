import sys
#from PyQt5.QtWidgets import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
class MyDlg(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,300,500)
        self.setWindowTitle("myTitle")
        layout = QVBoxLayout()
        l1 = QLabel('hello1')
        l2 = QLabel('hello2')
        button = QPushButton('btn1')
        button.clicked.connect( self.btn_click )
        edit = QLineEdit('edit1')
        layout.addWidget(l1)
        layout.addWidget(l2)
        layout.addWidget(button)
        layout.addWidget(edit)
        self.setLayout(layout)
    def btn_click(self):
        print('hello')
def main():
    app = QApplication(sys.argv)
    dlg = MyDlg()
    dlg.show()
    app.exec() #loop queue memory... 
if __name__ == '__main__':
    main()
    
    
    
    
    
    