import func

functions = {1:func.addInfo, 2:func.printInfo, 3:func.searchInfo}

def __main__():
    while True:
        print('''메인 메뉴)
    1.입력
    2.출력
    3.검색
    4.종료''')
        inputNum = int(input('번호를 입력하세요:'))
        
        if inputNum==4:
            break
        elif inputNum in range(1,4):
            functions[inputNum]();
        


__main__()