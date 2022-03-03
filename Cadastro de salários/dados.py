cadastro_por_mes = {
    "janeiro": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "fevereiro": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "Março": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "abril": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "maio": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "junho": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "julho": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "agosto": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "setembro": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "outubro": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "novembro": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    "dezembro": {
        "Nome": {},
        "Salário base": {},
        "Extras de segunda-sábado": {},
        "Valor total das extras tipo 1": {},
        "Taxa das extras tipo 1": {},
        "Extras nos domingos-feriados": {},
        "Valor total das extras tipo 2": {},
        "Taxa da extras tipo 2": {},
        "Bonificações": {},
        "Valor da bonificação": {}
    },
    }

def cadastrar_os_dados(mes, empregado, cadastro_por_mes):
    cadastro_por_mes[mes]["Nome"][empregado.nome] = empregado.nome
    cadastro_por_mes[mes]["Salário base"][empregado.nome] = empregado.salario[mes]
    cadastro_por_mes[mes]["Extras de segunda-sábado"][empregado.nome] = empregado.qtd_horas_extras_1[mes]
    cadastro_por_mes[mes]["Valor total das extras tipo 1"][empregado.nome] = empregado.valor_hora_extra_1[mes]
    cadastro_por_mes[mes]["Taxa das extras tipo 1"][empregado.nome] = empregado.taxa_hora_extra_1[mes]
    cadastro_por_mes[mes]["Extras nos domingos-feriados"][empregado.nome] = empregado.qtd_horas_extras_2[mes]
    cadastro_por_mes[mes]["Valor total das extras tipo 2"][empregado.nome] = empregado.valor_hora_extra_2[mes]
    cadastro_por_mes[mes]["Taxa da extras tipo 2"][empregado.nome] = empregado.taxa_hora_extra_2[mes]
    cadastro_por_mes[mes]["Bonificações"][empregado.nome] = "Sim" if empregado.bonificacoes[mes] == True else "Não"
    cadastro_por_mes[mes]["Valor da bonificação"][empregado.nome] = empregado.valor_bonificacoes[mes] if empregado.bonificacoes[mes]== True else 0.00