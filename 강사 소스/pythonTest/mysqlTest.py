import mysql.connector as MYSQL
def insertTable():
    try:
        config={'user':'root','password':'1234', 'host':'127.0.0.1','database':'world'}
        db = MYSQL.connect( **config )
        cur = db.cursor()
    #     q="insert into student(name, age, birth) values('임꺽정',30,'2000-01-20')"
        q="insert into student(name, age, birth) values(%s,%s,%s)"
    #     data = ('이순신', 40, '1971-06-06')
        datas = [('김철수1', 20, '1972-08-06'),('김철수2', 30, '1973-09-06'),('김철수3', 40, '1974-10-06')]
    #     cur.execute(q, data)
        cur.executemany(q, datas)
        db.commit()
        db.close()
        print("insert success")
    except Exception as err:
        print("error:",err)
def updateTable():
    try:
        config={'user':'root','password':'1234', 'host':'127.0.0.1','database':'world'}
        db = MYSQL.connect( **config )
        cur = db.cursor()
        q="update student set name='대한민국' where age=20"
        cur.execute(q)
        db.commit()
        db.close()
        print("update success")
    except Exception as err:
        print("error:",err)
def selectTable():
    try:
        config={'user':'root','password':'1234', 'host':'127.0.0.1','database':'world'}
        db = MYSQL.connect( **config )
        cur = db.cursor()
        q="select * from student"
        cur.execute(q)
        for n,a,b in cur:
            print(n,a,b)
            print(b.year, b.month, b.day )
#         data = cur.fetchall()
#         print(data)
        db.commit()
        db.close()
        print("select success")
    except Exception as err:
        print("error:",err)
if __name__ == '__main__':
    selectTable()


    
    
    
    
    
    
    
    