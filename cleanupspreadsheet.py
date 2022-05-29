import xlwt
import xlrd
book = xlrd.open_workbook('samples.xls')
first_sheet = book.sheet_by_index(0)
print(first_sheet.col_values(1))
first_sheet.write(0, 6, "NIF")
first_sheet.write(0, 6, "Points scored")
print(first_sheet.cell_value(0, 6))