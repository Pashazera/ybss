"""
    Author: Pashazera
    Time  : 2023/4/17 18:11
    File  : ygxsm.py
    describe :
"""


import  openpyxl as op



filename  = r'C:\Users\pashazera\Desktop\一标三实\数据\高新地址\余岗新市民公寓新一期业主信息综合表2022.07.08.xlsx'
ex = op.load_workbook(filename=filename,data_only=True)
data = ex[ex.sheetnames[0]]
wb = op.Workbook()
ws = wb.create_sheet('ygxsm',0)
print(data.cell(140,2).value)

for i in range(3,data.max_row):
    if data.cell(i,2).value is None and data.cell(i,4).value is None:
        data.cell(i,1,data.cell(i-1,1).value)
        data.cell(i,2,data.cell(i-1,2).value)
        data.cell(i, 3, data.cell(i - 1, 3).value)
        data.cell(i, 4, data.cell(i - 1, 4).value)
        data.cell(i, 5, data.cell(i - 1, 5).value)

    if data.cell(i,1).value is None and data.cell(i,7).value is None:
        break

ex.save('ygxsm.xlsx')


