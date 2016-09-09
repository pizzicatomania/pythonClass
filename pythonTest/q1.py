import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def btnClick():
    print('click')

app=QApplication(sys.argv)

mainDlg = QDialog()
mainDlg.setGeometry(300,300,300,500)
mainDlg.setWindowTitle('myTitle')

layout =QVBoxLayout()
l1 = QLabel('hello 1')
l2 = QLabel('hello 2')
button = QPushButton('button 1')
button.clicked.connect(btnClick)
edit =QLineEdit('edit 1')

layout.addWidget(l1)
layout.addWidget(l2)
layout.addWidget(button)
layout.addWidget(edit)

mainDlg.setLayout(layout)

mainDlg.show()



app.exec()
print('closed')