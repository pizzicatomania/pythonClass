import sqlite3
def createTable():
    try:
        db = sqlite3.connect('test.db') #데이터베이스가 없으면 만들고 open, 있으면 open
        cur = db.cursor()
        q= "create table student( name text, age int)"
        cur.execute(q)
        db.commit()
        db.close()
        print("create success")
    except Exception as err:
        print("err:",err)
        
def insertTable():
    try:
        db = sqlite3.connect('test.db') #데이터베이스가 없으면 만들고 open, 있으면 open
        cur = db.cursor()
#         q= "insert into student(name, age) values('임꺽정',30)"
        q= "insert into student(name, age) values( ?, ? )"
        data = ('이순신', 40)
        datas= [ ('김철수1', 20),('김철수2', 30),('김철수3', 40) ]
#         cur.execute(q, data )
        cur.executemany( q, datas)
        db.commit()
        db.close()
        print("insert success")
    except Exception as err:
        print("err:",err)
def updateTable():
    try:
        db = sqlite3.connect('test.db') #데이터베이스가 없으면 만들고 open, 있으면 open
        cur = db.cursor()
        q= "update student set name=? where age=20"
        data = ('김철수5',)
        cur.execute(q, data)
        db.commit()
        db.close()
        print("update success")
    except Exception as err:
        print("err:",err)
def deleteTable():
    try:
        db = sqlite3.connect('test.db') #데이터베이스가 없으면 만들고 open, 있으면 open
        cur = db.cursor()
        q= "delete from student where age=20"
        cur.execute(q)
        db.commit()
        db.close()
        print("delete success")
    except Exception as err:
        print("err:",err)
def selectTable():
    try:
        db = sqlite3.connect('test.db') #데이터베이스가 없으면 만들고 open, 있으면 open
        cur = db.cursor()
#         q= "select * from student"
#         q= "select * from student order by name desc"  #asc
#         q= "select * from student where age=30"  #asc
#         q= "select * from student where name like '%철%'"  #asc
        q = "select count(*) from student"
        cur.execute(q)
        n = cur.fetchone()
        print(n, n[0])
#         for n,a in cur:
#             print(n,a)
#         data = cur.fetchall()
#         print(data)
#         for n,a in data:
#             print(n, a)
        db.commit()
        db.close()
        print("select success")
    except Exception as err:
        print("err:",err)
if __name__ == '__main__':
    selectTable()        
        
        
        
        
        
        
        