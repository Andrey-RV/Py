#Programa de cadastro de salário de funcionários (em progresso)

from os import system

class Empregado:

    def __init__(self, nome):
        self.nome = nome
        self.salario={}
        self.hora_extra = False
        self.valor_extra = 0
        self.ferias = False
        self.bonificacoes = False
        self.valor_bonificacoes = 0
        self.porcentagem1=1.5
        self.porcentagem2=2

    @staticmethod
    def registrar_num_de_funcionarios():
        qtd_funcionarios=int(input("Insira o número de funcionários que serão cadastrados: "))
        while qtd_funcionarios<=0:
            qtd_funcionarios=int(input("Por favor, insira um número positivo de funcionários"))
        return qtd_funcionarios
    
    def sera_cadastrado(self, funcionario, mes):
        system('cls')
        cadastro=input(f"Deseja cadastrar os ganhos para o(a) funcionário(a) {funcionario.qual_nome()} no mês de {mes}? 'S' ou 'N': ")
        if cadastro=='N':
            return False
        return True
    
    def cadastrar_salario(self, funcionario):
        funcionario.salario=float(input("Qual o valor de seu salário base? R$"))

    def checar_hora_extra(self, funcionario):
        hora_extra=input(f"O funcionário(a) {funcionario.qual_nome()} fez horas extras neste mês? 'S' ou 'N': ")
        if hora_extra=="S":
            funcionario.hora_extra=True
    
    def checar_porcentagem_hora_extra(self):
        mudar_porcentagem=input("""Por padrão, as taxas mínimas de horas extras são de 50'%' para jornadas de segunda a sábado e 100% para domigos e feriados. Deseja alterar as porcentagens? 'S' ou 'N': """)
        if mudar_porcentagem=="S":
            return True
        return False
    
    def cadastrar_porcentagem_extra(self, funcionario):
        funcionario.porcentagem1=float(input("Insira a porcentagem para jornadas de segunda a sábado: "))
        funcionario.porcentagem2=float(input("Insira a porcentagem para jornadas domingo e feriados: "))
        funcionario.porcentagem1=1+funcionario.porcentagem1/100
        funcionario.porcentagem2=1+funcionario.porcentagem2/100
    
    def cadastrar_valor_extra(self, funcionario):
        extra_1=int(input("Quantas horas extras foram feitas de segunda a sábado? "))
        extra_2=int(input("Quantas horas extras foram feitas aos domingos ou feriados? "))
        funcionario.valor_extra=extra_1*funcionario.porcentagem1+extra_2*funcionario.porcentagem2

    def qual_nome(self):
        return self.nome
    
    def qual_salario(self):
        return self.salario
    
    def fez_hora_extra(self):
        return self.hora_extra
    
    def qual_valor_extra(self):
        return self.valor_extra
    
    def tirou_ferias(self):
        return self.ferias
    
    def recebeu_bonificacoes(self):
        return self.bonificacoes

    def qual_valor_bonificacoes(self):
        return self.valor_bonificacoes



funcionarios=[]
for num in range(Empregado.registrar_num_de_funcionarios()):
    funcionarios.append(Empregado(input(f"Digite o nome do(a) {num+1}º funcionário(a): ")))

meses=("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

for mes in meses:
    for funcionario in funcionarios:
        if not funcionario.sera_cadastrado(funcionario, mes):
            continue
        funcionario.cadastrar_salario(funcionario)
        funcionario.checar_hora_extra(funcionario)
        if funcionario.fez_hora_extra():
            if funcionario.checar_porcentagem_hora_extra():
                funcionario.cadastrar_porcentagem_extra(funcionario)
            funcionario.cadastrar_valor_extra(funcionario)
            


