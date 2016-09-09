from mymodule import *

def main():
    rst = gop(10, 20)
    print(rst)
    rst = hap(10, 20)
    print(rst)
    print("usemodule:", __name__ )
    print(type(__name__))

if __name__ == '__main__':
    main()
    
    
    
# import sys
# sys.path.append("E:\\pythonTest\\my")
# print(sys.path)
# import mymodule
# rst = mymodule.gop(10, 20)
# print(rst)
# rst = mymodule.hap(10, 20)
# print(rst)
