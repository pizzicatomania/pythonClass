import sqlite3

scoreList = [];
dbName= 'score.db' 

def addInfo():
    print('1) 입력')
    while True:
        name = input('이름: ')
        kor = int(input('국어: '))
        eng = int(input('영어: '))
        math = int(input('수학: '))
        
        try:
            db = sqlite3.connect(dbName)
            cur = db.cursor()
            q = "INSERT INTO grade(name, kor, eng, math) VALUES(?,?,?,?)"
            cur.execute(q,(name,kor,eng,math))
            db.commit()
            db.close()
        except Exception as err:
            print(err)
        
        scoreList.append({'name':name, 'kor':kor, 'eng':eng, 'math':math});
        
        cont = input('계속 입력하시겠습니까(y/n)? ')
        if cont == 'n':
            break;
        
    
def printInfo():
    print('2) 보기')
    printLine()
    for a in scoreList:
        print("  %s    %d    %d    %d    %d    %f" % (a['name'], a['kor'], a['eng'], a['math'], a['kor']+a['eng']+a['math'], (a['kor']+a['eng']+a['math'])/3))
    
def deleteInfo():
    print('3) 삭제')
    name = input('삭제 할 이름을 입력하세요: ')
    try:
        db = sqlite3.connect(dbName)
        cur = db.cursor()
        q = "DELETE FROM grade WHERE name=?"
        data = (name,)
        cur.execute(q,data)
        db.commit()
        db.close()
        
        for s in scoreList:
            if s['name']==name:
                scoreList.remove(s)
        
    except Exception as err:
        print(err)
    
def updateInfo():
    print('4) 수정')
#     name = input('수정 할 이름을 입력하세요: ')
#     try:
#         db = sqlite3.connect(dbName)
#         cur = db.cursor()
#         q = "SELECT * FROM grade WHERE name=?"
#         data = (name,)
#         cur.execute(q,data)
#         
#         score = cur.fetchone()
#         newName = input('이름(%s)' % (score['name']))
#         newKor= input('국어(%s)' % (score['kor']))
#         newEng = input('영어(%s)' % (score['eng']))
#         newMath = input('수학(%s)' % (score['math']))
#         
#         q = "UPDATE grade SET name=? kor=? eng=? math=? WHERE name=?"
#         data=(newName, newKor, newEng, newMath, name)
#         cur.execute(q,data)
#         db.commit()
#         db.close()
#         
#         for s in scoreList:
#             if s['name']==name:
#                 scoreList.remove(s)
#                 scoreList.append({'name':newName, 'kor':newKor, 'eng':newEng, 'math':newMath});
#                 break;
#         
#     except Exception as err:
#         print(err)
    
    
def searchInfo():
    print('5) 검색')
    name = input('검색 할 이름을 입력하세요: ')
    try:
        db = sqlite3.connect(dbName)
        cur = db.cursor()
        q = "SELECT * FROM grade WHERE name=?"
        data = (name,)
        cur.execute(q,data)
        score = cur.fetchall()
        db.close()
        printLine()
        
        for a in score:
            print("  %s    %d    %d    %d    %d    %f" % (a[0], a[1], a[2], a[3], a[1]+a[2]+a[3], (a[1]+a[2]+a[3])/3))
        
    except Exception as err:
        print(err)
        
def sortInfo():
    print('6) 정렬')
    sortTrue = input('정렬하시겠습니까(이름)? ')
    if sortTrue=='y':
        try:
            db = sqlite3.connect(dbName)
            cur = db.cursor()
            q = "SELECT * FROM grade ORDER BY name"
            cur.execute(q)
            score = cur.fetchall()
            db.close()
            printLine()
            
            for a in score:
                print("  %s    %d    %d    %d    %d    %f" % (a[0], a[1], a[2], a[3], a[1]+a[2]+a[3], (a[1]+a[2]+a[3])/3))
            
        except Exception as err:
            print(err)
    
def exitMain():
    print('7) 종료')
    sortTrue = input('종료하시겠습니까? ')
    if sortTrue=='y':
        exit()
    
def printLine():
    print('''=======================================================
  이름             국어      영어     수학    총점     평균
======================================================''')

functions = {1:addInfo, 2:printInfo, 3:deleteInfo, 4:updateInfo, 5:searchInfo, 6:sortInfo, 7:exitMain}

def initDB():
    
    try:
        db = sqlite3.connect(dbName)
        cur = db.cursor()
        q = "SELECT * FROM grade"
        cur.execute(q)
        data=cur.fetchall()
        for name,kor,eng,math in data:
            scoreList.append({"name":name,"kor":kor,"eng":eng,"math":math})
        db.close()
    except Exception as err:
        q = 'CREATE TABLE grade(name text, kor int, eng int, math int)'
        cur.execute(q)
        db.commit()
        db.close()

def __main__():
    initDB();
    while True:
        print('''==================
    성적데이터 처리
==================
    1.입력
    2.보기
    3.삭제
    4.수정
    5.검색
    6.정렬
    7.종료
    ''')
        inputNum = int(input('메뉴를 선택하세요:'))
        
        if inputNum in range(1,8):
            functions[inputNum]();
        


if __name__ == '__main__':
    __main__()