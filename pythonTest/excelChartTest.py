import openpyxl
from openpyxl.chart import BarChart, LineChart, PieChart, Series,Reference
wb = openpyxl.Workbook()
ws1 = wb.active
ws2 = wb.create_sheet("mysheet2")
ws1.append( ['number','title1','title2','title3'] )
ws1.append( [2,40,20,30] )
ws1.append( [3,20,40,20] )
ws1.append( [4,50,70,60] )
ws1.append( [5,60,30,80] )
ws1.append( [6,70,80,90] )
ws1.append( [7,80,20,20] )

chart1 = LineChart()
chart1.styles = 10
chart1.title = "Bar Chart"
chart1.x_axis.title = "x test"
chart1.y_axis.title = "y test"
data = Reference(ws1, min_col=2, min_row=1, max_row=7, max_col=4)
cat = Reference(ws1,min_col=1, min_row=2, max_row=7)
chart1.add_data(data,titles_from_data=True)
chart1.set_categories(cat)
ws1.add_chart(chart1,'F1')


ws2.append(['pie', 'sold'])
ws2.append(['Apple', 50])
ws2.append(['Cherry', 30])
ws2.append(['Banana',10])
ws2.append(['Orange', 40])
pie = PieChart()
labels = Reference(ws2, min_col=1, min_row=2, max_row=5)
data = Reference(ws2, min_col=2, min_row=1, max_row=5)
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)
pie.title = "Pie sold by test"
ws2.add_chart(pie, 'F1')

wb.save('mychart.xlsx')
print('write...')