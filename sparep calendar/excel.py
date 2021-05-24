from openpyxl import load_workbook

wb = load_workbook("C:\\00WORK FOLDER\\Github python projects\\sparep calendar\\data.xlsx")
#print(wb.sheet_ranges['E6'].value)
sheet_ranges = wb['Data']
print(sheet_ranges['A1'].value)
'''
ws= wb.active
ws.title = "data"

print(ws)
'''