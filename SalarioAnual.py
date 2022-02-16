#Programa de cadastro de salário de funcionários (em progresso)

from os import system


class Empregado:

    def __init__(self, nome):
        self.nome = nome
        self.salario_base={}
        self.qtd_horas_extras_1 = {}
        self.qtd_horas_extras_2 = {}
        self.valor_hora_extra_1 = {}
        self.valor_hora_extra_2 = {}
        self.tirou_ferias = {}
        self.recebeu_bonificacoes = {}
        self.valor_bonificacoes = 0
        self.taxa_hora_extra_1={"janeiro":1.5, "fevereiro":1.5, "março":1.5, "abril":1.5, "maio":1.5,  "junho":1.5, "julho":1.5, "agosto":1.5, "setembro":1.5, "outubro":1.5, "novembro":1.5, "dezembro":1.5,}
        self.taxa_hora_extra_2={"janeiro":2, "fevereiro":2, "março":2, "abril":2, "maio":2, "junho":2, "julho":2, "agosto":2, "setembro":2, "outubro":2, "novembro":2, "dezembro":2,}

    @staticmethod
    def registrar_num_de_funcionarios():
        qtd_funcionarios=int(input("Insira o número de funcionários que serão cadastrados: "))
        while qtd_funcionarios<=0:
            qtd_funcionarios=int(input("Por favor, insira um número positivo de funcionários"))
        return qtd_funcionarios

    
    def sera_cadastrado(self, funcionarios, mes):
        cadastro=input(f"Deseja cadastrar os ganhos para o(a) funcionário(a) {self.nome} no mês de {mes}? 'S' ou 'N': ")
        if cadastro=='N':
            situacao=input("Qual a situação do funcionário? Digite 'férias', 'demitido' ou 'nada' caso só deseje ignorar o cadastro esse mês: ")
            if situacao=='férias':
                self.tirou_ferias[mes]=True
                return False
            elif situacao=='demitido':
                self.tirou_ferias[mes]=False
                for i in range(len(funcionarios)):
                    if funcionarios[i].nome==self.nome:
                        funcionarios.pop(i)
                        break
                return False
            else:
                self.tirou_ferias[mes]=False
                return False
        return True

    
    def cadastrar_salario_base(self):
        if len(self.salario_base)>0:
            escolha_salario=input(f"Deseja alterar o salário de {self.salario_base[meses[meses.index(mes)-1]]}? 'S' ou 'N': ")
            if escolha_salario=='S':
                self.salario_base[mes]=float(input("Insira o novo salário: R$"))
            else:
                self.salario_base[mes]=self.salario_base[meses[meses.index(mes)-1]]
        else:
            self.salario_base[mes]=float(input("\nQual o valor de seu salário base? R$"))


    def checar_hora_extras(self):
        horas_extras=input(f"\nO funcionário(a) {self.nome} fez horas extras neste mês? 'S' ou 'N': ")
        if horas_extras=="S":
            return True
        return False
    

    def checar_taxas_hora_extra(self):
        mudar_porcentagem=input("""Por padrão, as taxas mínimas de horas extras são de 50% para jornadas de segunda a sábado e 100% para domigos e feriados. Deseja alterar as porcentagens? 'S' ou 'N': """)
        if mudar_porcentagem=="S":
            return True
        return False
    

    def cadastrar_porcentagem_extra(self):
        self.taxa_hora_extra_1[mes]=float(input("Insira a porcentagem para jornadas de segunda a sábado: "))
        while self.taxa_hora_extra_1[mes]<50:
            self.taxa_hora_extra_1[mes]=float(input("Você está inserindo um valor menor do que o permitido. Por favor, insira uma taxa de hora extra maior ou igual a 50%: "))
        self.taxa_hora_extra_2[mes]=float(input("Insira a porcentagem para jornadas domingo e feriados: "))
        while self.taxa_hora_extra_2[mes]<100:
            self.taxa_hora_extra_2[mes]=float(input("Você está inserindo um valor menor do que o permitido. Por favor, insira uma taxa de hora extra maior ou igual a 100%: "))
        self.taxa_hora_extra_1[mes]=1+self.taxa_hora_extra_1[mes]/100
        self.taxa_hora_extra_2[mes]=1+self.taxa_hora_extra_2[mes]/100
    

    def cadastrar_valor_hora_extra(self):
        extra_1=int(input("\nQuantas horas extras foram feitas de segunda a sábado? "))
        extra_2=int(input("Quantas horas extras foram feitas aos domingos ou feriados? "))
        self.valor_hora_extra_1[mes]=extra_1*self.taxa_hora_extra_1[mes]
        self.valor_hora_extra_2[mes]=extra_2*self.taxa_hora_extra_2[mes]


meses=("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

funcionarios=[]
for num in range(Empregado.registrar_num_de_funcionarios()):
    funcionarios.append(Empregado(input(f"Digite o nome do(a) {num+1}º funcionário(a): ")))
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
        if funcionario.checar_hora_extras():
            if funcionario.checar_taxas_hora_extra():
                funcionario.cadastrar_porcentagem_extra()
            funcionario.cadastrar_valor_hora_extra()
            


