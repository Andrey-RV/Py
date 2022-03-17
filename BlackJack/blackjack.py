class BlackJack:
    def __init__(self, baralho):
        self.cartas = baralho

    @staticmethod
    def contabilizar_pontos_dealer_nao_estourou(pontos_do_dealer, *pontuacoes):
        vencedores = []
        empates = []
        perdedores = []
        for pontuacao in pontuacoes:
            if pontuacao > pontos_do_dealer and pontuacao <= 21:
                vencedores.append(pontuacoes.index(pontuacao))
            elif pontuacao == pontos_do_dealer and pontuacao:
                empates.append(pontuacoes.index(pontuacao))
            else:
                perdedores.append(pontuacoes.index(pontuacao))
        for vencedor in vencedores:
            print(f"    O jogador {vencedor+1} ganhou")
        for empate in empates:
            print(f"    O jogador {empate+1} empatou")
        for perdedor in perdedores:
            print(f"    O jogador {perdedor+1} perdeu")
    
    @staticmethod
    def contabilizar_pontos_dealer_estourou(pontos_do_dealer, *pontuacoes):
        vencedores = []
        perdedores = []
        for pontuacao in pontuacoes:
            if pontuacao < pontos_do_dealer and pontuacao <= 21:
                vencedores.append(pontuacoes.index(pontuacao))
            else:
                perdedores.append(pontuacoes.index(pontuacao))
        for vencedor in vencedores:
            print(f"    O jogador {vencedor+1} ganhou")
        for perdedor in perdedores:
            print(f"    O jogador {perdedor+1} perdeu")