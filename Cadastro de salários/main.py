from os import system
from class_empregado import Empregado, meses
from openpyxl import Workbook, load_workbook
import excel

#TODO: ajustar o salvamento (TRUE/FALSE) de férias e bonificações

work_book = load_workbook("Funcionarios.xlsx")

funcionarios=[]

for num in range(Empregado.registrar_num_de_funcionarios()):
    funcionarios.append(Empregado(input(f"Digite o nome do(a) {num+1}º funcionário(a): ")))

excel.salvar_funcionarios_no_arquivo(work_book, funcionarios, meses)
excel.salvar_arquivo(work_book)

for mes in meses:
    system('cls')
    cadastro_mensal=input(f"\nDeseja prosseguir com o cadastro para o mês de {mes}? Insira 'S ou 'N': ")
    if cadastro_mensal=='N': continue
    for funcionario in funcionarios:
        system('cls')
        if not funcionario.sera_cadastrado(funcionarios, mes): continue
        funcionario.cadastrar_salario_base(mes)
        if funcionario.recebeu_bonificacoes():
            funcionario.cadastrar_bonificacoes(mes)
        if funcionario.fez_hora_extra():
            if funcionario.taxa_hora_extra_nao_eh_padrao():
                funcionario.cadastrar_porcentagem_extra(mes)
            funcionario.cadastrar_valor_hora_extra(mes)
            


