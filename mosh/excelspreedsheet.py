import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell_1 = sheet['a1']
#cell_1 =
print(cell_1)