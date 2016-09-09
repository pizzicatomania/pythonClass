import pandas as pd

d= [0,1,2,3,4,5,6,7,8,9]
d1=[10,20,30]
d2=[100,200,300]
d3=[1000,2000,3000]


df = pd.DataFrame(d,columns=["my1"] ,index=['a','b','c','d','e','f','g','h','i','j'],)

# print(df['my1'])

df1 = pd.DataFrame()
sr1 = pd.Series(d1)
sr2 = pd.Series(d2)
sr3 = pd.Series(d3)
df1['col1']=sr1
df1['col2']=sr2
df1['col3']=sr3
df1.index = ['a','b','c']

df1.columns = ['aaa','bbb','ccc']
print(df1)
# print(df1.head(2))
# print(df1.tail(2))
# print(df1)
# print(df1['col2'])
# print(df1[['col2','col3']])
# print(df1.ix[0:2, ['col1', 'col3']])
# print(df1.loc[['a','c']])