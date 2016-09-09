import pandas as pd

myDic ={"LG":[1010,2010,900,400,500], 
        "LG1":[5678,2010,900,400,500],
        "LG2":[999,2010,900,400,500],
        }

myDicIdx = ['15-01','15-02','15-03','15-04','15-05']
colm = ['LG2','LG1','LG']
df = pd.DataFrame( myDic, columns=colm, index =myDicIdx )

print(df)
print('='*30)
print(df.describe())
# print(df.sum())
# print(df['LG'].sum())
# print(df.ix[0:2, ['LG', 'LG1']].sum())
# print(df.ix['15-03'].sum())

# df.to_csv('pp.csv')
# df.to_excel("pd.xlsx")
# print(df['LG'])
# print(df.T)
# print(df.ix['15-03'])