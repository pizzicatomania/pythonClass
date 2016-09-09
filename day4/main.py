import pandas as pd
import matplotlib.pyplot as mlp

scoreList = pd.DataFrame()

def addInfo():
    print('1. 입력')
    global scoreList
    scoreDict={}
    while True:
        name = input('이름: ')
        kor = int(input('국어: '))
        eng = int(input('영어: '))
        math = int(input('수학: '))
        scoreDict[name]=[kor,eng,math]

        cont = input('계속 입력하시겠습니까(y/n)? ')
        if cont == 'n':
            scoreList = pd.DataFrame(scoreDict,index =['국어','영어','수학'])
            break;
        
    
def printInfo():
    print('2. 출력')
    printLine()
    for a in scoreList.columns:
        print(" %s  %d   %d   %d   %d   %f" % (a, scoreList[a].loc['국어'], scoreList[a].loc['영어'], scoreList[a].loc['수학'], scoreList[a].sum(), scoreList[a].mean()))
    
def printStat():
    print('3. 통계')
    print(scoreList.describe())
    scoreList.plot(kind='bar')
    mlp.show()

    
def printLine():
    print('''=======================================================
  이름        국어      영어     수학    총점     평균
======================================================''')

functions = {1:addInfo, 2:printInfo, 3:printStat}

def __main__():
    while True:
        print('''메인 메뉴)
    1.입력
    2.출력
    3.통계
    4.종료''')
        inputNum = int(input('번호를 입력하세요:'))
        
        if inputNum==4:
            break
        elif inputNum in range(1,4):
            functions[inputNum]();
        


if __name__ == '__main__':
    __main__()