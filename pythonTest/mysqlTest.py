import mysql.connector as MYSQL
try:
    config={'user':'root', 'password':'1234', 'host':'127.0.0.1','database':'world'}
    db = MYSQL.connect(**config)
    cur = db.cursor()
#     q = "insert into student(name, age, birth) values(%s,%s,%s)"
#     data = [('ccc',44,'1888-04-03'),('ddd',45,'1888-04-01'),('eee',14,'1888-03-03'),('fff',22,'1238-12-13')]
#     cur.executemany(q, data)
#     q = "UPDATE student SET name='qqq' WHERE age=45"
    q = "SELECT * FROM student WHERE age='45'"
    cur.execute(q)
    for n,a,b in cur:
        print(n,a,b)
        print(b.year, b.month, b.day)
#     print(cur.fetchall())
    db.commit();
    db.close()
    print('success')
    
except Exception as err:
    print(err)