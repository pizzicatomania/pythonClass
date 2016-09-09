import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MyDlg(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,300,500)
        self.setWindowTitle('myTitle')

        layout =QVBoxLayout()
        l1 = QLabel('hello 1')
        l2 = QLabel('hello 2')
        button = QPushButton('button 1')
        button.clicked.connect(self.btn_click)
        edit =QLineEdit('edit 1')
        
        layout.addWidget(l1)
        layout.addWidget(l2)
        layout.addWidget(button)
        layout.addWidget(edit)
        
        self.setLayout(layout)
        
    def btn_click(self):
        print('clicked')


def main():
    app=QApplication(sys.argv)
    dlg = MyDlg()
    dlg.show()
    
    app.exec()


if __name__=='__main__':
    main()

print('closed')