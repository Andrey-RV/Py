from os import system
from random import randint

class TicTacToe:
    O=["O", "O", "O"]
    X=["X", "X", "X"]
    linhas = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    colunas = []
    diagonais = []

    def salva_linhas(self):
        linha=int(input("Digite em qual linha deseja jogar: "))
        coluna=int(input("Digite em qual coluna deseja jogar: "))
        while self.linhas[linha-1][coluna-1]!="_":
            print("A posição já está preenchida. Por favor, selecione casa desocupada")
            linha=int(input("Digite em qual linha deseja jogar: "))
            coluna=int(input("Digite em qual coluna deseja jogar: "))
        self.linhas[linha-1][coluna-1]=self.identificacao

    @classmethod
    def imprime_tabuleiro(cls):
        print("\n")
        for linha in cls.linhas:
            print(linha)
        print("\n")
    
    @classmethod
    def salva_colunas(cls):
        cls.colunas.append([cls.linhas[0][0], cls.linhas[1][0], cls.linhas[2][0]])
        cls.colunas.append([cls.linhas[0][1], cls.linhas[1][1], cls.linhas[2][1]])
        cls.colunas.append([cls.linhas[0][2], cls.linhas[1][2], cls.linhas[2][2]])
    
    @classmethod
    def salva_diagonais(cls):
        cls.diagonais.append([cls.linhas[0][0], cls.linhas[1][1], cls.linhas[2][2]])
        cls.diagonais.append([cls.linhas[0][2], cls.linhas[1][1], cls.linhas[2][0]])

    @classmethod
    def checar_empate(cls):
        if "_" not in TicTacToe.linhas[0] and "_" not in TicTacToe.linhas[1] and "_" not in TicTacToe.linhas[2]:
            return True
    
    def registrar_empate(self):
        print(f"Empate, o placar está  {p1.quantas_vitorias()} para o jogador 1, e {p2.quantas_vitorias()} para o jogador 2\n")

    @classmethod
    def checar_vitoria(cls):
        if (cls.O in cls.linhas or cls.O in cls.colunas or cls.O in cls.diagonais):
            if p1.identificacao=="O":
                p1.salva_vitoria()
            else:
                p2.salva_vitoria()
            return "O"
        elif (cls.X in cls.linhas or cls.X in cls.colunas or cls.X in cls.diagonais):
            if p1.identificacao=="X":
                p1.salva_vitoria()
            else:
                p2.salva_vitoria()
            return "X"
        else:
            return "next!"
    
    def registrar_vitoria(self):
        print(f"Parabéns!, o placar está  {p1.quantas_vitorias()} para o jogador 1, e {p2.quantas_vitorias()} para o jogador 2\n")

    @classmethod
    def limpa_tabuleiro(cls):
        cls.linhas=[["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        cls.colunas=[["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        cls.diagonais=[["_", "_", "_"], ["_", "_", "_"]]

class Jogador(TicTacToe):
    def __init__(self):
        self.identificacao=""
        self.qtd_de_vitorias=0

    @staticmethod
    def escolha():
        escolha1=input("O jogador 1 será O ou X? ")
        if escolha1=="O":
            p1.identificacao="O"
            p2.identificacao="X"
        else:
            p1.identificacao="X"
            p2.identificacao="O"

    def salva_vitoria(self):
        self.qtd_de_vitorias+=1
    
    def quantas_vitorias(self):
        return self.qtd_de_vitorias

class Computador(Jogador):
    def salva_linhas(self):
        linha=randint(0,3)
        coluna=randint(0,3)
        while self.linhas[linha-1][coluna-1]!="_":
            linha=randint(0,3)
            coluna=randint(0,3)
        self.linhas[linha-1][coluna-1]=self.identificacao


modo_de_jogo=input("Insira '1' se deseja jogar contra o computador, ou '2' se deseja jogar contra um amigo: ")
if modo_de_jogo=="1":
    p2=Computador()
elif modo_de_jogo=="2":
    p2=Jogador()

p1=Jogador()
Jogador.escolha()
continuar_o_jogo='S'
system('cls')

while continuar_o_jogo=='S' or continuar_o_jogo=="s":
    while True:
        system('cls')
        print("Sua vez de jogar, jogador1!")
        TicTacToe.imprime_tabuleiro()
        p1.salva_linhas()
        TicTacToe.salva_colunas()
        TicTacToe.salva_diagonais()
        if TicTacToe.checar_vitoria()!="next!":
            p1.registrar_vitoria()
            break
        system('cls')
        if TicTacToe.checar_empate():
            p1.registrar_empate()
            break

        print("Sua vez de jogar, jogador2!")
        TicTacToe.imprime_tabuleiro()
        p2.salva_linhas()
        TicTacToe.salva_colunas()
        TicTacToe.salva_diagonais()
        if TicTacToe.checar_vitoria()!="next!":
            p2.registrar_vitoria()
            break
    
    continuar_o_jogo=input("Deseja continuar o jogo? Insira 'S' ou 'N': ")
    TicTacToe.limpa_tabuleiro()