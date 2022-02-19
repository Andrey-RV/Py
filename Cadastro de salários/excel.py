from openpyxl import Workbook, load_workbook
   
work_book = Workbook()
work_sheet= work_book.active
cell_range = work_sheet['A1':'K1']

def salvar_funcionarios_no_arquivo(funcionarios):
    for index in range(len(funcionarios)):
        cell_range[0][index].value=funcionarios[index].nome

def salvar_arquivo():
    work_book.save('Funcionarios.xlsx')