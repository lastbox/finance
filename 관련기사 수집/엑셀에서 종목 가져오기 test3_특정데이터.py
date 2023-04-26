import openpyxl as xl

wb = xl.load_workbook('D:/lastBox/당일 거래대금 1000억 이상/당일 거래대금 1000억 이상 xlsx/거래대금 1000억 이상_2023-04-26 14-39-$S.xlsx')
sheet = wb['Sheet']

# print('['+sheet.cell(row=1, column=2).value+']')
# print('['+sheet['A2'].value+']')
# 
print('sheet.row', sheet.rows)
print('=' * 50)

for row in sheet.rows:
    print(row.value)
print('=' * 50)

for data in sheet['A1':'B1']:
    for cell in data:
        print('['+cell.value+']')

print('=' * 50)

# A1부터 B2 데이터까지 가져오기
for data in sheet['A1':'B2']:
    for cell in data:
        print('['+cell.value+']')

wb.close()