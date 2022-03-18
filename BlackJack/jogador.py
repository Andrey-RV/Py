from random import SystemRandom
random = SystemRandom()


class Jogador:
    def __init__(self, cartas):
        self.pontuacao = 0
        self.mao = []
        self.mao_inicial(cartas)
    
    def mao_inicial(self, cartas):
        self.mao.append(random.choice(cartas))
        cartas.remove(self.mao[-1])
        self.mao.append(random.choice(cartas))
        cartas.remove(self.mao[-1])
        self.pontuacao = (self.mao[0] + self.mao[1])

    def mostrar_mao_e_pontuacao(self, numero_do_jogador):
        print(f"  Mão do jogador {numero_do_jogador}: {self.mao}, sua pontuação atual é: {self.pontuacao}")

    def cavar_carta(self, cartas, numero_do_jogador):
        self.mao.append(random.choice(cartas))
        cartas.remove(self.mao[-1])
        self.atualizar_pontuacao()
        self.mostrar_mao_e_pontuacao(numero_do_jogador)
    
    def atualizar_pontuacao(self):
        if self.mao[-1] == 11:
            escolha = input("Você retirou um Ás. Deseja que ele valha 1 ou 11 pontos? Insira '1' ou '11': ")
            if escolha == "1":
                self.mao[-1] = 1
                self.pontuacao += 1
            else:
                self.pontuacao += 11
        else:
            self.pontuacao += self.mao[-1]
    
    def estourou(self):
        if self.pontuacao > 21:
            return True
        return False
    
    def reiniciar_o_jogo(self, cartas):
        self.mao = []
        self.mao_inicial(cartas)