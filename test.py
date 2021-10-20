# print('this is a pen')


import xlrd

book = xlrd.open_workbook('testbook001.xlsx')

# シートの数
print("Sheet num: ", end='')
print(book.nsheets)

s1 = book.sheet_by_index(0)

# 行と列を取得
print("sheet1 cols: " + str(s1.ncols))
print("sheet1 rows: " + str(s1.nrows))

# sheet1のB3を取得
print("sheet1,B3: ",s1.cell(2,1).value)
