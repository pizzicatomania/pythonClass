import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

class MyDlg:
    def __init__(self):
        self.ui = uic.loadUi('c.ui')
        self.ui.pushButton.clicked.connect(self.btn_click)
        self.ui.listWidget.currentItemChanged.connect(self.btn_click)
        self.ui.comboBox.currentIndexChanged.connect(self.onComboChange)
        self.ui.radioButtonRed.clicked.connect(self.onRadioClick)
        self.ui.radioButtonBlue.clicked.connect(self.onRadioClick)
        self.ui.radioButtonYellow.clicked.connect(self.onRadioClick)
        
        self.initWidget()
        self.initTable()
        self.ui.show()
        
    def initTable(self):
        self.ui.tableWidget.setColumnCount(2)
#         self.ui.tableWidget.setRowCount(2)
#         self.ui.tableWidget.setHorizontalHeaderLabels(['이름', '나이'])
#         self.ui.tableWidget.setItem(0,0,QTableWidgetItem('이상민'))
#         self.ui.tableWidget.setItem(0,1,QTableWidgetItem('29'))
#         self.ui.tableWidget.setItem(1,0,QTableWidgetItem('쭌빢횽'))
#         self.ui.tableWidget.setItem(1,1,QTableWidgetItem('129'))
        self.tableData('dltkdals', 23)
        self.tableData('qkrwnsgyd', 34)
        self.tableData('wnsePD', 44)
    
    def tableData(self,name,age):
        nRow = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(nRow+1)
        self.ui.tableWidget.setItem(nRow,0,QTableWidgetItem(name))
        self.ui.tableWidget.setItem(nRow,1,QTableWidgetItem(str(age)))
    
    def initWidget(self):
        self.ui.listWidget.addItems(['LG', 'LG1', 'LG2'])
        self.ui.listWidget.addItem('LG3')    
        self.ui.comboBox.addItems(['LG', 'LG1', 'LG2'])
        self.ui.comboBox.addItem('LG3')
        
    def onRadioClick(self):
        if self.ui.radioButtonRed.isChecked():
            print("red")
        if self.ui.radioButtonBlue.isChecked():
            print("blue")
        if self.ui.radioButtonYellow.isChecked():
            print("Yellow")
        
    def onComboChange(self):
        txt = self.ui.comboBox.currentText()
        self.ui.lineEdit.setText(txt)
            
    def btn_click(self):
#         txt = self.ui.listWidget.currentItem().text()
        d = self.ui.dateTimeEdit.date()
        t = self.ui.dateTimeEdit.time()
        print(d.year(), d.month(), d.day())
        print(t.hour(), t.minute(), t.second())
#         self.ui.lineEdit.setText(txt)
        

def main():
    app=QApplication(sys.argv)
    dlg = MyDlg()
    
    app.exec()


if __name__=='__main__':
    main()

print('closed')