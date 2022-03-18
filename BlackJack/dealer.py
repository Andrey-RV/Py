from random import SystemRandom
from jogador import Jogador
random = SystemRandom()


class Dealer(Jogador):
    """Agrupa métodos que manipulam a mão e a pontuação do dealer."""
    def __init__(self, cartas):
        super().__init__(cartas) 
    
    def mao_inicial(self, cartas):
        """Adiciona uma carta inicial à mão do dealer e a remove do baralho."""
        self.mao.append(random.choice(cartas))
        cartas.remove(self.mao[-1])
        self.pontuacao = self.mao[0]
    
    def mostrar_mao_e_pontuacao(self):
        """Imprime a mão e a pontuação final do dealer."""
        print(f"  A mão do dealer é: {self.mao}, a pontuação do dealer é: {self.pontuacao}")
    
    def cavar_carta(self, cartas):
        """Adiciona cartas à mão do dealer e as remove do baralho enquanto a pontuação do dealer for inferior a 17.\n\nChama o método atualizar_pontuacao() para atualizar a pontuacao do dealer após cada nova carta cavada."""
        while self.pontuacao < 17:
            self.mao.append(random.choice(cartas))
            cartas.remove(self.mao[-1])
            self.atualizar_pontuacao()
        self.mostrar_mao_e_pontuacao()

    def atualizar_pontuacao(self):
        """Atualiza a pontuação do dealer com base na última carta adicionada à sua mão."""
        if self.mao[-1] == 11 and self.pontuacao + 11 >=17 and self.pontuacao + 11 <= 21:
            self.pontuacao += 11
        elif self.mao[-1] == 11:
            self.mao[-1] = 1
            self.pontuacao += 1
        else:
            self.pontuacao += self.mao[-1]
        
    def reiniciar_o_jogo(self, cartas):
        """Limpa a mão do dealer e o entrega uma primeira carta para recomeçar a partida."""
        self.mao = []
        self.mao_inicial(cartas)