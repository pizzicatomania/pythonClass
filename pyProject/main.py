from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
import func
import sys
import sqlite3

dbName= 'book.db' 
functions = {1:func.addInfo, 2:func.printInfo, 3:func.printStat}

class AddDlg:
    def __init__(self):
        self.ui = uic.loadUi("detail_view.ui")
        self.ui.btn_ok.clicked.connect(self.ok_clicked)
        self.ui.btn_add.clicked.connect(self.ok_clicked)
        self.ui.btn_cancel.clicked.connect(self.cancel_clicked)
        self.ui.exec() # modal
    
    def ok_clicked(self):
        try:
            db = sqlite3.connect(dbName)
            cur = db.cursor()
            q = "INSERT INTO books(id, date, name, publisher, author, category, etc) VALUES(?,?,?,?,?,?,?)"
            cur.execute(q,(self.ui.lineEdit_bookId.text(),
                           self.ui.dateEdit.text(),
                           self.ui.lineEdit_bookName.text(),
                           self.ui.lineEdit_bookPublisher.text(),
                           self.ui.lineEdit_bookAuthor.text(),
                           self.ui.lineEdit_bookCat.text(),
                           self.ui.lineEdit_bookEtc.text()))
            db.commit()
            db.close()
        except Exception as err:
            print(err)
            
        self.ui.close()
    
    def cancel_clicked(self):
        self.ui.close()

class SearchDlg:
    def __init__(self):
        self.query = 'id'
        self.ui = uic.loadUi("search.ui")
        self.ui.comboBox.addItems(['관리번호', '도서명'])
        self.ui.comboBox.currentIndexChanged.connect(self.onComboChange)
        self.ui.pushButton.clicked.connect(self.pushButtonClicked)
        self.clearTable()
        self.ui.exec() # modal
        
    def pushButtonClicked(self):
        self.clearTable()
        self.searchInfo()
        
    def clearTable(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(['관리번호', '등록일', '도서명', '출판사', '저자', '도서종류', '비고'])
        
    def searchInfo(self):
        try:
            db = sqlite3.connect(dbName)
            cur = db.cursor()
            q = "SELECT * FROM books WHERE "
            if self.query=='id':
                q = q+" id = ?"
            else:
                q = q+" name = ?"
            
            data = (self.ui.lineEdit.text(),)
            cur.execute(q,data)
            books = cur.fetchall()
            db.close()
            
            for b in books:
                self.tableData(b)
            
        except Exception as err:
            print(err)
    
    def tableData(self,d):
        nRow = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(nRow+1)
        self.ui.tableWidget.setItem(nRow,0,QTableWidgetItem(d[0]))
        self.ui.tableWidget.setItem(nRow,1,QTableWidgetItem(d[1]))
        self.ui.tableWidget.setItem(nRow,2,QTableWidgetItem(d[2]))
        self.ui.tableWidget.setItem(nRow,3,QTableWidgetItem(d[3]))
        self.ui.tableWidget.setItem(nRow,4,QTableWidgetItem(d[4]))
        self.ui.tableWidget.setItem(nRow,5,QTableWidgetItem(d[5]))
        self.ui.tableWidget.setItem(nRow,6,QTableWidgetItem(d[6]))
    
    def onComboChange(self):
        if self.ui.comboBox.currentText()=='관리번호':
            self.query = 'id'
        else:
            self.query = 'name'
    

class MainDlg:
    def __init__(self):
        self.ui = uic.loadUi('BookManager.ui')
        self.ui.actionAdd.triggered.connect(self.openAdd)
        self.ui.actionSearch.triggered.connect(self.openSearch)
        
        self.initDB()
        self.ui.show()
    def openAdd(self):
        dlg = AddDlg()
        self.initDB()
        
    def openSearch(self):
        dlg = SearchDlg()
        self.initDB()
        


    def initDB(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(['관리번호', '등록일', '도서명', '출판사', '저자', '도서종류', '비고'])
        try:
            db = sqlite3.connect(dbName)
            cur = db.cursor()
            q = "SELECT * FROM books"
            cur.execute(q)
            data=cur.fetchall()
            for d in data:
                self.tableData(d)
            db.close()
        except Exception as err:
            print(err)
            q = 'CREATE TABLE books(id text, date text, name text, publisher text, author text, category text, etc text)'
            cur.execute(q)
            db.commit()
            db.close()
    def tableData(self,d):
        nRow = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(nRow+1)
        self.ui.tableWidget.setItem(nRow,0,QTableWidgetItem(d[0]))
        self.ui.tableWidget.setItem(nRow,1,QTableWidgetItem(d[1]))
        self.ui.tableWidget.setItem(nRow,2,QTableWidgetItem(d[2]))
        self.ui.tableWidget.setItem(nRow,3,QTableWidgetItem(d[3]))
        self.ui.tableWidget.setItem(nRow,4,QTableWidgetItem(d[4]))
        self.ui.tableWidget.setItem(nRow,5,QTableWidgetItem(d[5]))
        self.ui.tableWidget.setItem(nRow,6,QTableWidgetItem(d[6]))

def main():
    app=QApplication(sys.argv)
    dlg = MainDlg()
    
    app.exec()

        

if __name__ == '__main__':
    main()