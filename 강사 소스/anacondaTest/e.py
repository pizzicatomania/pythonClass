import pandas as pd
import matplotlib.pyplot as mlp
import pandas.io.data as data
import datetime
# from pandas_datareader import data, wb
startDate = datetime.datetime(2016,7,1)
endDate = datetime.datetime(2016,8,31)
dr = data.DataReader('003550.KS','yahoo', 
                     startDate, endDate )

mlp.plot(dr.index, dr['Open'],'r--', dr.index, dr['Close'],'b-')
mlp.xlabel('date')
mlp.ylabel('stock')
mlp.title('LG')
mlp.show()












# dr.plot(kind='line')
# mlp.show()

# print(dr)
# print(dr['Open'])
