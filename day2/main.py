import openpyxl
from openpyxl.chart import BarChart, Reference

scoreList = [];
fileName = 'myScore.xlsx' 

def addInfo():
    print('1. 입력')
    while True:
        name = input('이름: ')
        kor = int(input('국어: '))
        eng = int(input('영어: '))
        scoreList.append({'name':name, 'kor':kor, 'eng':eng});
        cont = input('계속 입력하시겠습니까(y/n)? ')
        if cont == 'n':
            break;
        
    
def printInfo():
    print('2. 출력')
    printLine()
    for a in scoreList:
        print("  %(name)s    %(kor)d    %(eng)d" % a)
    
    
def saveExcel():
    wb = openpyxl.Workbook()
    ws1 = wb.active
    ws1.append( ['이름','국어','영어'] )
    for s in scoreList:
        ws1.append( [s['name'], s['kor'], s['eng'] ] )
    
    chart1 = BarChart()
    chart1.styles = 10
    chart1.title = "이름별 성적"
    chart1.x_axis.title = "이름"
    chart1.y_axis.title = "점수"
    data = Reference(ws1, min_col=2, min_row=1, max_row=len(scoreList)+1, max_col=3)
    cat = Reference(ws1,min_col=1, min_row=2, max_row=len(scoreList)+1)
    chart1.add_data(data,titles_from_data=True)
    chart1.set_categories(cat)
    ws1.add_chart(chart1,'F1')
    
    wb.save(fileName)
    print('save as', fileName)

    
def printLine():
    print('''--------------------------------
    이름        국어        영어
-------------------------------''')

functions = {1:addInfo, 2:printInfo, 3:saveExcel}

def __main__():
    while True:
        print('''메인 메뉴)
    1.입력
    2.출력
    3.엑셀저장(이름별 성적 바차트 포함)
    4.종료''')
        inputNum = int(input('번호를 입력하세요:'))
        
        if inputNum==4:
            break
        elif inputNum in range(1,4):
            functions[inputNum]();
        


if __name__ == '__main__':
    __main__()