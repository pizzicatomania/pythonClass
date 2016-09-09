import pandas

myList=[10,20,30,40,50,60,70,80,90]
sr = pandas.Series(myList, name='mySeries')
sr1 = pandas.Series([1010, 2010, 3010,4010], index=['15-01','15-02','15-03','15-04'])
sr2 = pandas.Series({'a':0,'b':1,'c':2})
print(sr.sum())
print(sr.mean())
print(sr.median())
print(sr.std())
print(sr.var())
print(sr.min())
print(sr.max())

# print(sr[sr>30])

# print(sr.at[0])
# print(sr2.ix[0])
# print(sr2.ix['a'])

# print(sr1)
# print(sr1.iloc[0:2])
# print(sr2.loc['a':'b'])

# print(sr.at[0])
# print(sr2.at['a'])
# print(sr2.iat[0])

# print(sr.index)
# print(sr.values)
# print(sr.ndim)
# print(sr.size)
# print(sr.name)

# sr.values = pandas.Series([100,200,300,400]).values

# print(sr)
# print(sr1.index)
# print(sr2.index)

# sr[0]=100
# print(sr)
# print(sr[0])
# print(sr1['15-01'])
# print(sr2['a'])

# sr.index = ['a','b','c','d']
# print(sr)
# print(sr1)
# print(sr2)