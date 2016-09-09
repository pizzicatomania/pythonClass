import sqlite3

def createTable():
    try:
        db = sqlite3.connect('test.db')
        cur = db.cursor()
        q = 'CREATE TABLE student(name text, age int)'
        cur.execute(q)
        db.commit()
        db.close()
        print('create success')
    except Exception as err:
        print("err:", err)
        
        
def insertTable():
    try:
        db = sqlite3.connect('test.db')
        cur = db.cursor()
#         q = "INSERT INTO student(name, age) values('laaaa', 32)"
        q = "INSERT INTO student(name, age) values(?, ?)"
#         data = ('asd',45)
        dataList = [('asd',45),('bnm',43),('cvb',54)]
#         cur.execute(q, data)
        cur.executemany(q, dataList)
        db.commit()
        db.close()
        print('insert success')
    except Exception as err:
        print("err:", err)

def updateTable():
    try:
        db = sqlite3.connect('test.db')
        cur = db.cursor()
        q = "UPDATE student SET name=? WHERE age=45"
        data=('bbb',)
        cur.execute(q,data)
        db.commit()
        db.close()
        print('update success')
    except Exception as err:
        print("err:", err)

def deleteTable():
    try:
        db = sqlite3.connect('test.db')
        cur = db.cursor()
        q = "DELETE FROM student WHERE age=45"
        cur.execute(q)
        db.commit()
        db.close()
        print('delete success')
    except Exception as err:
        print("err:", err)

def selectTable():
    try:
        db = sqlite3.connect('test.db')
        cur = db.cursor()
#         q = "SELECT * FROM student ORDER BY name DESC"
#         q = "SELECT * FROM student WHERE age=54"
#         q = "SELECT * FROM student WHERE name LIKE '%a%'"
        q = "SELECT COUNT(*) FROM student"
        cur.execute(q)
        n=cur.fetchone()
        print(n[0])
#         data=cur.fetchall()
#         for n,a in data:
#             print(n,a)
        
        
        for n,a in cur:
            print(n,a)
        
        db.close()
        print('select success')
    except Exception as err:
        print("err:", err)
        
if __name__== '__main__':
    selectTable()