addrList = [];


def addInfo():
    print('1. 입력')
    while True:
        name = input('이름: ')
        age = int(input('나이: '))
        addr = input('주소: ')
        addrList.append({'name':name, 'age':age, 'addr':addr});
        cont = input('계속 입력하시겠습니까(y/n)? ')
        if cont == 'n':
            break;
        
    
def printInfo():
    print('2. 출력')
    print('''--------------------------------
    이름        나이        주소
-------------------------------''')
    for a in addrList:
        print("  %(name)s    %(age)d    %(addr)s" % a)
    
    
def searchInfo():
    print('3. 검색')
    query = input('검색할 이름을 입력하세요:')
    print('''--------------------------------
    이름        나이        주소
-------------------------------''')
    for a in addrList:
        if a['name'] == query:
            print("  %(name)s    %(age)d    %(addr)s" % a)
            
    
    