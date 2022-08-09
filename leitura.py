import openpyxl

book=openpyxl.load_workbook('computador.xlsx')
frutas_page=book['computadores']

for rows in frutas_page.iter_rows(min_row=2):
    for cell in rows:
        print(cell.value)