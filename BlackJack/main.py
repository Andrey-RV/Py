#TODO: debugar os erros que acontecem quando o jogador escolhe continuar o jogo algumas vezes:
#      1 - O método randint falha aleatoriamente após algumas repetições;
#      2 - Numeração incorreta no número dos jogadores que ganharam/empataram/perderam

from os import system
from logo_e_baralho import logo, baralho_52_cartas
from blackjack import BlackJack
from jogador import Jogador
from dealer import Dealer


while True:
    blackjack = BlackJack(baralho_52_cartas)
    dealer = Dealer(blackjack.cartas)
    quantidade_de_jogadores = int(input("Quantos jogadores irão jogar? "))
    jogadores = [Jogador(blackjack.cartas) for x in range(quantidade_de_jogadores)]
    system('cls')
    print(logo)

    for jogador in jogadores:
        print(f"    É a vez do jogador {jogadores.index(jogador) + 1}")
        jogador.mostrar_mao_e_pontuacao()
        dealer.mostrar_mao_e_pontuacao()
        while True:
            cavar = input("\nDigite 'c' para cavar mais uma carta, ou 'p' para encerrar sua jogada: ")
            if cavar == 'p': break
            jogador.cavar_carta(blackjack.cartas)
            if jogador.estourou(): break
        system('cls')
        print(logo)
    dealer.cavar_carta(blackjack.cartas)

    for jogador in jogadores:
        jogador.mostrar_mao_e_pontuacao()
    pontuacoes = [jogador.pontuacao for jogador in jogadores]
    if dealer.estourou():
        blackjack.contabilizar_pontos_dealer_estourou(dealer.pontuacao, *pontuacoes)
    else:
        blackjack.contabilizar_pontos_dealer_nao_estourou(dealer.pontuacao, *pontuacoes)

    choice=input("\nDeseja jogar novamente? 's' or 'n': ")
    if choice == 'n':
        break