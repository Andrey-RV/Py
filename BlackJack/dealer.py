from random import SystemRandom
from jogador import Jogador
random = SystemRandom()


class Dealer(Jogador):
    def __init__(self, cartas):
        super().__init__(cartas) 
    
    def mao_inicial(self, cartas):
        self.mao.append(random.choice(cartas))
        cartas.remove(self.mao[-1])
        self.pontuacao = self.mao[0]
    
    def mostrar_mao_e_pontuacao(self):
        print(f"  A mão do dealer é: {self.mao}, a pontuação do dealer é: {self.pontuacao}")
    
    def cavar_carta(self, cartas):
        self.mao.append(random.choice(cartas))
        cartas.remove(self.mao[-1])
        self.atualizar_pontuacao()
        while self.pontuacao < 17:
            self.mao.append(random.choice(cartas))
            cartas.remove(self.mao[-1])
            self.atualizar_pontuacao()
        self.mostrar_mao_e_pontuacao()

    def atualizar_pontuacao(self):
        if self.mao[-1] == 11 and self.pontuacao + 11 >=17 and self.pontuacao + 11 <= 21:
            self.pontuacao += 11
        elif self.mao[-1] == 11:
            self.mao[-1] = 1
            self.pontuacao += 1
        else:
            self.pontuacao += self.mao[-1]
        
    def reiniciar_o_jogo(self, cartas):
        self.mao = []
        self.mao_inicial(cartas)