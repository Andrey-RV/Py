from os import system
from random import randint
from dataclasses import dataclass


@dataclass
class Tabuleiro:
    O=["O", "O", "O"]
    X=["X", "X", "X"]
    linhas = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    colunas = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    diagonais = [["_", "_", "_"], ["_", "_", "_"]]

    @classmethod
    def imprime_tabuleiro(cls):
        print("\n")
        for linha in cls.linhas:
            print(linha)
        print("\n")

    @classmethod
    def checa_o_tabuleiro(cls):
        if (cls.O in cls.linhas or cls.O in cls.colunas or cls.O in cls.diagonais):
            return "O"
        elif (cls.X in cls.linhas or cls.X in cls.colunas or cls.X in cls.diagonais):
            return "X"
        else:
            return "next!"

    @classmethod
    def limpa_tabuleiro(cls):
        cls.linhas=[["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        cls.colunas=[["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        cls.diagonais=[["_", "_", "_"], ["_", "_", "_"]]


class Jogador:
    def __init__(self):
        self.identificacao=""
        self.qtd_de_vitorias=0
       
    def quantas_vitorias(self):
        return self.qtd_de_vitorias

    def checa_empate():
        if "_" not in Tabuleiro.linhas[0] and "_" not in Tabuleiro.linhas[1] and "_" not in Tabuleiro.linhas[2]:
            return True

    def registra_empate(self):
            print(f"Empate, o placar está {p1.quantas_vitorias()} para o jogador 1 e {p2.quantas_vitorias()} para o jogador 2")
    
    def registra_vitoria(self):
        if Tabuleiro.checa_o_tabuleiro()=="X":
            if p1.identificacao=="X":
                p1.qtd_de_vitorias+=1
            else:
                p2.qtd_de_vitorias+=1
        if Tabuleiro.checa_o_tabuleiro()=="O":
            if p1.identificacao=="O":
                p1.qtd_de_vitorias+=1
            else:
                p2.qtd_de_vitorias+=1
        print(f"Parabéns, o placar está {p1.quantas_vitorias()} para o jogador 1 e {p2.quantas_vitorias()} para o jogador 2") 


class Humano(Jogador):
    @staticmethod
    def identificiacao():
        escolha=input("O jogador 1 será O ou X? ")
        if escolha=="O":
            p1.identificacao="O"
            p2.identificacao="X"
        else:
            p1.identificacao="X"
            p2.identificacao="O"

    def salva_elemento(self):
        linha=int(input("Digite em qual linha deseja jogar: "))
        coluna=int(input("Digite em qual coluna deseja jogar: "))
        while Tabuleiro.linhas[linha-1][coluna-1]!="_":
            print("A posição já está preenchida. Por favor, selecione casa desocupada")
            linha=int(input("Digite em qual linha deseja jogar: "))
            coluna=int(input("Digite em qual coluna deseja jogar: "))
        Tabuleiro.linhas[linha-1][coluna-1]=self.identificacao
        Tabuleiro.colunas.append([Tabuleiro.linhas[0][0], Tabuleiro.linhas[1][0], Tabuleiro.linhas[2][0]])
        Tabuleiro.colunas.append([Tabuleiro.linhas[0][1], Tabuleiro.linhas[1][1], Tabuleiro.linhas[2][1]])
        Tabuleiro.colunas.append([Tabuleiro.linhas[0][2], Tabuleiro.linhas[1][2], Tabuleiro.linhas[2][2]])
        Tabuleiro.diagonais.append([Tabuleiro.linhas[0][0], Tabuleiro.linhas[1][1], Tabuleiro.linhas[2][2]])
        Tabuleiro.diagonais.append([Tabuleiro.linhas[0][2], Tabuleiro.linhas[1][1], Tabuleiro.linhas[2][0]])

class Computador(Jogador):
    @staticmethod
    def identificiacao():
        escolha=input("Deseja jogar com X ou O? ")
        if escolha=="O":
            p1.identificacao="O"
            p2.identificacao="X"
        else:
            p1.identificacao="X"
            p2.identificacao="O"

    def salva_elemento(self):
        linha=randint(0,2)
        coluna=randint(0,2)
        while Tabuleiro.linhas[linha][coluna]!="_":
            linha=randint(0,2)
            coluna=randint(0,2)
        Tabuleiro.linhas[linha][coluna]=self.identificacao
        Tabuleiro.colunas.append([Tabuleiro.linhas[0][0], Tabuleiro.linhas[1][0], Tabuleiro.linhas[2][0]])
        Tabuleiro.colunas.append([Tabuleiro.linhas[0][1], Tabuleiro.linhas[1][1], Tabuleiro.linhas[2][1]])
        Tabuleiro.colunas.append([Tabuleiro.linhas[0][2], Tabuleiro.linhas[1][2], Tabuleiro.linhas[2][2]])
        Tabuleiro.diagonais.append([Tabuleiro.linhas[0][0], Tabuleiro.linhas[1][1], Tabuleiro.linhas[2][2]])
        Tabuleiro.diagonais.append([Tabuleiro.linhas[0][2], Tabuleiro.linhas[1][1], Tabuleiro.linhas[2][0]])


p1=Humano()
modo_de_jogo=input("Insira '1' se deseja jogar solo, ou '2' se deseja jogar com outra pessoa: ")
p2=Computador() if modo_de_jogo=="1" else Humano()
p2.identificiacao()
continuar_o_jogo='S'

while continuar_o_jogo=='S' or continuar_o_jogo=="s":
    while True:
        system('cls')
        print("Sua vez de jogar, jogador1!")
        Tabuleiro.imprime_tabuleiro()
        p1.salva_elemento()
        if Tabuleiro.checa_o_tabuleiro()!="next!":
            system('cls')
            Tabuleiro.imprime_tabuleiro()
            p1.registra_vitoria()
            break
        elif Jogador.checa_empate():
            system('cls')
            Tabuleiro.imprime_tabuleiro()
            p1.registra_empate()
            break
        system('cls')
        print("Sua vez de jogar, jogador2!")
        Tabuleiro.imprime_tabuleiro()
        p2.salva_elemento()
        if Tabuleiro.checa_o_tabuleiro()!="next!":
            system('cls')
            Tabuleiro.imprime_tabuleiro()
            p2.registra_vitoria()
            break
    
    continuar_o_jogo=input("Deseja continuar o jogo? Insira 'S' ou 'N': ")
    Tabuleiro.limpa_tabuleiro()