import pandas as pd

df1 = pd.DataFrame()
def add1():
    d1 =[10,20,30]
    sr1 = pd.Series(d1)
    df1['col1']= sr1
#     df1.index = ['a','b','c']
def add2():
    d2 =[100,200,300]
    sr2 = pd.Series(d2)
    df1['col2']= sr2
#     df1.index = ['a','b','c']
def add3():
    d3 =[1000,2000,3000]
    sr3 = pd.Series(d3)
    df1['col3']= sr3
    df1.index = ['a','b','c']
#     df1.columns = ['aaa','bbb','ccc']
if __name__ == '__main__':
    add1()
    add2()
    add3()
    print(df1)












