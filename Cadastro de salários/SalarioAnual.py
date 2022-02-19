from os import system
from class_empregado import Empregado, meses
import excel


funcionarios=[]
for num in range(Empregado.registrar_num_de_funcionarios()):
    funcionarios.append(Empregado(input(f"Digite o nome do(a) {num+1}º funcionário(a): ")))

excel.salvar_funcionarios_no_arquivo(funcionarios)
excel.salvar_arquivo()

for mes in meses:
    system('cls')
    cadastro_mensal=input(f"\nDeseja prosseguir com o cadastro para o mês de {mes}? Insira 'S ou 'N': ")
    if cadastro_mensal=='N':
        continue
    for funcionario in funcionarios:
        system('cls')
        if not funcionario.sera_cadastrado(funcionarios, mes):
            continue
        funcionario.cadastrar_salario_base()
        if funcionario.checar_bonificacoes():
            funcionario.cadastrar_bonificacoes()
        if funcionario.checar_hora_extras():
            if funcionario.checar_taxas_hora_extra():
                funcionario.cadastrar_porcentagem_extra()
            funcionario.cadastrar_valor_hora_extra()
            


