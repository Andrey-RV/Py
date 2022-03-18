class BlackJack:
    """Possui como atributo único uma lista com as cartas que serão utilizadas no jogo, além de métodos relacionados à analise das pontuações finais, discriminando os venceores, empates e perdedores."""
    def __init__(self, baralho):
        self.cartas = baralho

    @staticmethod
    def contabilizar_pontos_dealer_nao_estourou(pontos_do_dealer, *pontuacoes):
        """Imprime os vencedores, empates e perdedores após comparar seus pontos com os pontos do dealer."""
        vencedores = []
        empates = []
        perdedores = []
        for i in range(len(pontuacoes)):
            if pontuacoes[i] > pontos_do_dealer and pontuacoes[i] <= 21:
                vencedores.append(i)
            elif pontuacoes[i] == pontos_do_dealer and pontuacoes[i] <= 21:
                empates.append(i)
            else:
                perdedores.append(i)
        for vencedor in vencedores:
            print(f"    O jogador {vencedor+1} ganhou")
        for empate in empates:
            print(f"    O jogador {empate+1} empatou")
        for perdedor in perdedores:
            print(f"    O jogador {perdedor+1} perdeu")
    
    @staticmethod
    def contabilizar_pontos_dealer_estourou(pontos_do_dealer, *pontuacoes):
        """Imprime os vencedores e perdedores após comparar seus pontos com os pontos do dealer."""
        vencedores = []
        perdedores = []
        for i in range(len(pontuacoes)):
            if pontuacoes[i] < pontos_do_dealer and pontuacoes[i] <= 21:
                vencedores.append(i)
            else:
                perdedores.append(i)
        for vencedor in vencedores:
            print(f"    O jogador {vencedor+1} ganhou")
        for perdedor in perdedores:
            print(f"    O jogador {perdedor+1} perdeu")