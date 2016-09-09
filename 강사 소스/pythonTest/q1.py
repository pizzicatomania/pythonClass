import sys
#from PyQt5.QtWidgets import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def btnClick():
    print("click....")
app = QApplication(sys.argv)
mainDlg = QDialog()
mainDlg.setGeometry(300,300,300,500)
mainDlg.setWindowTitle("myTitle")
layout = QVBoxLayout()
l1 = QLabel('hello1')
l2 = QLabel('hello2')
button = QPushButton('btn1')
button.clicked.connect( btnClick )
edit = QLineEdit('edit1')

layout.addWidget(l1)
layout.addWidget(l2)
layout.addWidget(button)
layout.addWidget(edit)

mainDlg.setLayout(layout)
mainDlg.show()

app.exec() #loop queue memory... 
print('hello')










