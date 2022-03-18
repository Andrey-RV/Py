from os import system
from logo_e_baralho import logo, baralho_52_cartas
from blackjack import BlackJack
from jogador import Jogador
from dealer import Dealer


quantidade_de_jogadores = int(input("Quantos jogadores irão jogar? "))
blackjack = BlackJack(baralho=quantidade_de_jogadores*baralho_52_cartas)
dealer = Dealer(cartas=blackjack.cartas)
jogadores = [Jogador(blackjack.cartas) for x in range(quantidade_de_jogadores)]
system('cls')
print(logo)

while True:
    for i in range(len(jogadores)):
        print(f"    É a vez do jogador {i+1}")
        jogadores[i].mostrar_mao_e_pontuacao(numero_do_jogador=i+1)
        dealer.mostrar_mao_e_pontuacao()
        while True:
            cavar = input("\nDigite 'c' para cavar mais uma carta, ou 'p' para encerrar sua jogada: ")
            if cavar == 'p': break
            jogadores[i].cavar_carta(cartas=blackjack.cartas, numero_do_jogador=i+1)
            if jogadores[i].estourou(): break
        pontuacoes = [jogador.pontuacao for jogador in jogadores]
        system('cls')
        print(logo)

    for i in range(len(jogadores)):
        jogadores[i].mostrar_mao_e_pontuacao(numero_do_jogador=i+1)

    dealer.cavar_carta(cartas=blackjack.cartas)
    if dealer.estourou():
        blackjack.contabilizar_pontos_dealer_estourou(dealer.pontuacao, *pontuacoes)
    else:
        blackjack.contabilizar_pontos_dealer_nao_estourou(dealer.pontuacao, *pontuacoes)

    choice=input("\nDeseja jogar novamente? 's' or 'n': ")
    if choice == 'n':
        break
    else:
        blackjack.cartas = quantidade_de_jogadores * baralho_52_cartas
        dealer.reiniciar_o_jogo(cartas=blackjack.cartas)
        for i in range(len(jogadores)):
            jogadores[i].reiniciar_o_jogo(cartas=blackjack.cartas)