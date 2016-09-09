# import sys
# # sys.path.append("D:\\pythonTest\\my")
# import myModule
# print(sys.path)
# 
# print(myModule.gop(10,20))
# print(myModule.hap(10,20))

from myModule import *


def main():
    print("useModule:", __name__)

if __name__ == '__main__':
    main();

# print(type(__name__))