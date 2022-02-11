from os import system

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
            print("A posição já está preenchida. Por favor, joga selecione casa desocupada")
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

    @classmethod
    def limpa_tabuleiro(cls):
        cls.linhas = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

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


p1=Jogador()
p2=Jogador()
Jogador.escolha()
continuar_o_jogo='S'
system('cls')

while continuar_o_jogo=='S' or continuar_o_jogo=="s":
    while True:
        print("Sua vez de jogar, jogador1!")
        TicTacToe.imprime_tabuleiro()
        p1.salva_linhas()
        TicTacToe.salva_colunas()
        TicTacToe.salva_diagonais()
        system('cls')
        if TicTacToe.checar_vitoria()!="next!":
            break
        print("Sua vez de jogar, jogador2!")
        TicTacToe.imprime_tabuleiro()
        p2.salva_linhas()
        system('cls')
        if TicTacToe.checar_vitoria()!="next!":
            break
        TicTacToe.salva_colunas()
        TicTacToe.salva_diagonais()

    print(f"Parabéns!, o placar está  {p1.quantas_vitorias()} para o jogador 1, e {p2.quantas_vitorias()} para o jogador 2\n")
    continuar_o_jogo=input("Deseja continuar o jogo? Insira 'S' ou 'N': ")
    TicTacToe.limpa_tabuleiro()