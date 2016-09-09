import pandas as pd
import matplotlib.pyplot as mlp
x1 = [ 1,2,3,4,5,6 ]
y1 = [ 6,5,7,8,9,10 ]
x2 = [ 1,2,3,4,5,6 ]
y2 = [ 6,5,7,8,9,10 ]
fg = mlp.figure()

ax = fg.add_subplot( 2,1,1 ) #row, column, figureNum
ax.bar(x1, y1, color='red')

ay = fg.add_subplot( 2,1,2 )
ay.plot(x2,y2, color='blue')
mlp.show()






# df = pd.read_excel('pd.xlsx')
# print(df)
# 
# x1 =[1,2,3,4,5]
# x2 = df.index
# mlp.xticks(x1, x2)
# mlp.bar(x1, df['LG'], align='center', color='red' )
# mlp.show()

# x1 = [0,1,2,3]
# xLabel=['aa','bb','cc','dd']
# mlp.xticks(x1,xLabel)
# mlp.plot( x1 ,[10,3,20,8] )
# mlp.show()

# df = pd.read_excel('pd.xlsx')
# print(df)
# df.plot(kind='line')
# mlp.show()




# datas = [{"name": "홍길동", "age": 20}, 
# df = pd.DataFrame(datas)
# # print(df)
# df.index = df['name']
# df.pop('name')
# print(df)












