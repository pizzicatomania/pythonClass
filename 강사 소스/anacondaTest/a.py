import pandas
myList = [10,20,30,40,50,60,70,80,90]
sr = pandas.Series(myList, name="myseries")
sr1 = pandas.Series([1010,2010,3010,4010], 
                    index=['15-01','15-02','15-03','15-04'] )
sr2 = pandas.Series( {'a':0,'b':1,'c':2 } )
print( sr.sum() )
print( sr.mean() )
print( sr.median() )
print( sr.min() )
print( sr.max() )
print( sr.std() ) #표준편차
print( sr.var() ) #분산
# print( sr[sr>30] )

# print(sr1)
# print( sr1.iloc[0:2] )
# print( sr2.loc['a':'c'] )

# print( sr.at[0] ) # sr[0]
# print( sr.ix[0] ) # sr[0]
# print( sr2.ix['a'] ) #sr2['a']

# print( sr2.at['a'] )
# print( sr2.iat[0] )
# print(sr2)


# print( sr2.T )
# print(sr.index)
# print(sr.values)
# print( sr.ndim )
# print( sr.size )
# print( sr.name)
# print(sr)

# print(type(sr.values))
# sr.values = pandas.Series([100,200,300,400]).values

# sr[0] = 100
# print(sr)
# print( sr[0] )
# print( sr1['15-01'])
# print(sr2['a'])
# sr.index = ['a','b','c','d']
# print(sr2)
# print(sr)
# print(sr1)
