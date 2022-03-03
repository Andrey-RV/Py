meses_do_ano=("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

class Empregado:
    def __init__(self, nome):
        self.nome = nome
        self.salario={}
        self.qtd_horas_extras_1 = {}
        self.valor_hora_extra_1 = {}
        self.taxa_hora_extra_1={"janeiro":1.5, "fevereiro":1.5, "março":1.5, "abril":1.5, "maio":1.5,  "junho":1.5, "julho":1.5, "agosto":1.5, "setembro":1.5, "outubro":1.5, "novembro":1.5, "dezembro":1.5,}
        self.qtd_horas_extras_2 = {}
        self.valor_hora_extra_2 = {}
        self.taxa_hora_extra_2={"janeiro":2, "fevereiro":2, "março":2, "abril":2, "maio":2, "junho":2, "julho":2, "agosto":2, "setembro":2, "outubro":2, "novembro":2, "dezembro":2,}
        self.bonificacoes = {}
        self.valor_bonificacoes = {}

    @staticmethod
    def registrar_num_de_funcionarios():
        qtd_funcionarios=int(input("Insira o número de funcionários que serão cadastrados: "))
        while qtd_funcionarios<=0:
            qtd_funcionarios=int(input("Por favor, insira um número positivo de funcionários"))
        return qtd_funcionarios

    
    def sera_cadastrado(self, funcionarios, mes):
        cadastro=input(f"Deseja cadastrar os ganhos para o(a) funcionário(a) {self.nome} no mês de {mes}? 'S' ou 'N': ")
        if cadastro=='N':
            situacao=input("Qual a situação do funcionário? Digite 'demitido' ou 'nada' caso só deseje ignorar o cadastro esse mês: ")
            if situacao=='demitido':
                for i in range(len(funcionarios)):
                    if funcionarios[i].nome==self.nome:
                        funcionarios.pop(i)
                        break
                return False
            else:
                return False
        return True

    
    def cadastrar_salario(self, mes):
        if len(self.salario)>0:
            escolha_salario=input(f"Deseja alterar o salário de {self.salario[meses_do_ano[meses_do_ano.index(mes)-1]]}? 'S' ou 'N': ")
            if escolha_salario=='S':
                self.salario[mes]=float(input("Insira o novo salário: R$"))
            else:
                self.salario[mes]=self.salario[meses_do_ano[meses_do_ano.index(mes)-1]]
        else:
            self.salario[mes]=float(input("\nQual o valor de seu salário base? R$"))

    
    def recebeu_bonificacoes(self, mes):
        bonificacao=input(f"\nO funcionário(a) {self.nome} recebeu alguma bonificação esse mês? 'S' ou 'N': ")
        if bonificacao=="S":
            self.bonificacoes[mes]=True
            return True
        self.bonificacoes[mes]=False
        return False


    def cadastrar_bonificacoes(self, mes):
        extra_1=float(input("\nQuantas o funcionário recebeu de bonificações? "))
        self.valor_bonificacoes[mes]=extra_1


    def fez_hora_extra(self, mes):
        horas_extras=input(f"\nO funcionário(a) {self.nome} fez horas extras neste mês? 'S' ou 'N': ")
        if horas_extras=="S":
            return True
        self.qtd_horas_extras_1[mes]=0
        self.valor_hora_extra_1[mes]=0
        self.taxa_hora_extra_1[mes]=0
        self.qtd_horas_extras_2[mes]=0
        self.valor_hora_extra_2[mes]=0
        self.taxa_hora_extra_2[mes]=0
        return False
    

    def taxa_hora_extra_nao_eh_padrao(self):
        mudar_porcentagem=input("""Por padrão, as taxas mínimas de horas extras são de 50% para jornadas de segunda a sábado e 100% para domigos e feriados. Deseja alterar as porcentagens? 'S' ou 'N': """)
        if mudar_porcentagem=="S":
            return True
        return False
    

    def cadastrar_porcentagem_extra(self, mes):
        self.taxa_hora_extra_1[mes]=float(input("Insira a porcentagem para jornadas de segunda a sábado: "))
        while self.taxa_hora_extra_1[mes]<50:
            self.taxa_hora_extra_1[mes]=float(input("Você está inserindo um valor menor do que o permitido. Por favor, insira uma taxa de hora extra maior ou igual a 50%: "))
        self.taxa_hora_extra_2[mes]=float(input("Insira a porcentagem para jornadas domingo e feriados: "))
        while self.taxa_hora_extra_2[mes]<100:
            self.taxa_hora_extra_2[mes]=float(input("Você está inserindo um valor menor do que o permitido. Por favor, insira uma taxa de hora extra maior ou igual a 100%: "))
        self.taxa_hora_extra_1[mes]=1+self.taxa_hora_extra_1[mes]/100
        self.taxa_hora_extra_2[mes]=1+self.taxa_hora_extra_2[mes]/100
    

    def cadastrar_valor_hora_extra(self, mes):
        self.qtd_horas_extras_1[mes]=int(input("\nQuantas horas extras foram feitas de segunda a sábado? "))
        self.qtd_horas_extras_2[mes]=int(input("Quantas horas extras foram feitas aos domingos ou feriados? "))
        self.valor_hora_extra_1[mes]=self.qtd_horas_extras_1[mes]*self.taxa_hora_extra_1[mes]*(self.salario[mes]/220)
        self.valor_hora_extra_2[mes]=self.qtd_horas_extras_2[mes]*self.taxa_hora_extra_2[mes]*(self.salario[mes]/220)