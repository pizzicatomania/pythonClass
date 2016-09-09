import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
class MyDlg:
    def __init__(self):
        self.ui = uic.loadUi("c.ui") #xml ==>객체화
        self.ui.pushButton.clicked.connect( self.btn_click )
        self.ui.listWidget.currentItemChanged.connect( self.btn_click )
        self.ui.comboBox.currentIndexChanged.connect( self.onComboChange )
        self.ui.radioButtonRed.clicked.connect( self.onRadioClick )
        self.ui.radioButtonBlue.clicked.connect( self.onRadioClick )
        self.ui.radioButtonYellow.clicked.connect( self.onRadioClick )
        self.initWidget()
        self.initTable()
        self.ui.show()
    def initTable(self):
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels( ['이름','나이'] )
#         self.ui.tableWidget.setRowCount (2)
#         self.ui.tableWidget.setItem( 0,0, QTableWidgetItem('홍길동') )
#         self.ui.tableWidget.setItem( 0,1, QTableWidgetItem('30') )
#         self.ui.tableWidget.setItem( 1,0, QTableWidgetItem('이순신') )
#         self.ui.tableWidget.setItem( 1,1, QTableWidgetItem('40') )
        self.tableData('홍길동', 30)
        self.tableData('이순신', 40)
        self.tableData('김철수', 50)
    def tableData(self, name, age):
        nRow = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(nRow+1)
        self.ui.tableWidget.setItem( nRow,0, QTableWidgetItem(name) )
        self.ui.tableWidget.setItem( nRow,1, QTableWidgetItem( str(age)) )
        
    def initWidget(self):
        self.ui.listWidget.addItems( ['LG','LG1','LG2'] )
        self.ui.listWidget.addItem('LG3')
        self.ui.comboBox.addItems( ['LG','LG1','LG2'] )
        self.ui.comboBox.addItem( 'LG3' )
    def onRadioClick(self):
        if self.ui.radioButtonRed.isChecked():
            print("red...")
        if self.ui.radioButtonBlue.isChecked():
            print('blue')
        if self.ui.radioButtonYellow.isChecked():
            print('yellow')
    def onComboChange(self):
        txt = self.ui.comboBox.currentText()
        self.ui.lineEdit.setText(txt)
    def btn_click(self):
#         txt = self.ui.listWidget.currentItem().text()
        d = self.ui.dateTimeEdit.date()
        t = self.ui.dateTimeEdit.time()
        print( d.year(), d.month(), d.day())
        print( t.hour(), t.minute(), t.second())        
#         self.ui.lineEdit.setText(txt)
     
def main():
    app = QApplication(sys.argv)
    dlg = MyDlg()
    app.exec() #loop queue memory... 
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    