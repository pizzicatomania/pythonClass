class Address:
    datas = []
    def input_data(self):
        while True:
            name = input("이름:")
            age = int(input("나이:"))
            yn= input("계속입력(y/n):")
            self.datas.append({'name':name, 'age':age})
            if yn == 'n':
                break
    
    def output_data(self):
        for data in self.datas:
            print( "%(name)10s%(age)10d"% data )
if __name__ == '__main__':
    addr = Address()
    addr.input_data()
    addr.output_data()
#     input_data()
#     output_data()