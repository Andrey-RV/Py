from os import system
from empregados import Empregado, meses_do_ano
from dados import cadastro_por_mes, cadastrar_os_dados
import pandas

funcionarios = []

for num in range(Empregado.registrar_num_de_funcionarios()):
    funcionarios.append(Empregado(input(f"Digite o nome do(a) {num+1}º funcionário(a): ")))

for mes in meses_do_ano:
    # system('cls')
    cadastro_mensal=input(f"\nDeseja prosseguir com o cadastro para o mês de {mes}? Insira 'S ou 'N': ")
    if cadastro_mensal=='N': continue
    for funcionario in funcionarios:
        system('cls')
        if not funcionario.sera_cadastrado(funcionarios, mes): continue
        funcionario.cadastrar_salario(mes)
        if funcionario.recebeu_bonificacoes(mes):
            funcionario.cadastrar_bonificacoes(mes)
        if funcionario.fez_hora_extra(mes):
            if funcionario.taxa_hora_extra_nao_eh_padrao():
                funcionario.cadastrar_porcentagem_extra(mes)
            funcionario.cadastrar_valor_hora_extra(mes)
        cadastrar_os_dados(mes, funcionario, cadastro_por_mes)
        cadastro_por_mes_DataFrame=pandas.DataFrame(cadastro_por_mes[mes])
        cadastro_por_mes_DataFrame.to_excel("cadastro_mensal.xlsx", index=False)