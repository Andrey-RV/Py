from openpyxl import Workbook, load_workbook
   

def salvar_funcionarios_no_arquivo(work_book ,funcionarios, meses):
    for mes in meses:
        work_sheet=work_book[mes]
        cell_range = work_sheet['B1':'L1']
        for index in range(len(funcionarios)):
            cell_range[0][index].value=funcionarios[index].nome

def salvar_arquivo(work_book):
    work_book.save('Funcionarios.xlsx')