from random import SystemRandom
random = SystemRandom()


class Jogador:
    """Agrupa métodos que manipulam as mãos e as pontuações de cada jogador."""
    def __init__(self, cartas):
        self.pontuacao = 0
        self.mao = []
        self.mao_inicial(cartas)
    
    def mao_inicial(self, cartas):
        """Adiciona duas cartas iniciais à mão do jogador e as remove do baralho."""
        self.mao.append(random.choice(cartas))
        cartas.remove(self.mao[-1])
        self.mao.append(random.choice(cartas))
        cartas.remove(self.mao[-1])
        self.pontuacao = (self.mao[0] + self.mao[1])

    def mostrar_mao_e_pontuacao(self, numero_do_jogador):
        """Imprime a mão e a pontuação do jogador."""
        print(f"  Mão do jogador {numero_do_jogador}: {self.mao}, sua pontuação atual é: {self.pontuacao}")

    def cavar_carta(self, cartas, numero_do_jogador):
        """Adiciona uma carta à mão do jogador e a remove do baralho.\n\nChama o método atualizar_pontuacao() para atualizar a pontuação do jogador após a adição da carta à sua mão."""
        self.mao.append(random.choice(cartas))
        cartas.remove(self.mao[-1])
        self.atualizar_pontuacao()
        self.mostrar_mao_e_pontuacao(numero_do_jogador)
    
    def atualizar_pontuacao(self):
        """Atualiza a pontuação do jogador com base na última carta adicionada à sua mão.\n\nCaso o jogador tenha cavado um ás, verifica por meio de um input se o jogador deseja que esta valha 1 ou 11 pontos."""
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
        """Verifica se a pontuação do jogador ultrapassou os 2 pontos, retornando True caso o tenha feito."""
        if self.pontuacao > 21:
            return True
        return False
    
    def reiniciar_o_jogo(self, cartas):
        """Limpa a mão do jogador e o entrega duas novas cartas para recomeçar a partida."""
        self.mao = []
        self.mao_inicial(cartas)