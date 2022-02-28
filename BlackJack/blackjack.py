from random import SystemRandom
from os import system
from BlackJack.art import logo


def mostrar_pontuacao(minha_mao, pontuacao, mao_pc, pontuacao_pc):
    print(f"  Sua mão atual é: {minha_mao}, sua pontuação atual é: {pontuacao}")
    print(f"  A mão atual do computado é: {mao_pc}, a pontuação atual do computador é: {pontuacao_pc}")


def cavar_carta(minha_mao, mao_pc, cartas, pontuacao, pontuacao_pc):
    minha_mao.append(cartas[random.randint(0, len(cartas)-1)])
    cartas.remove(minha_mao[-1])
    if pontuacao_pc<pontuacao and pontuacao<=21:
        mao_pc.append(cartas[random.randint(0, len(cartas)-1)])
        cartas.remove(mao_pc[-1])
        return True
    return False


def pc_cava(cartas, mao_pc):
    contagem_de_cartas_cavadas_pc=0
    if pontuacao<=21:
        mao_pc.append(cartas[random.randint(0, len(cartas)-1)])
        cartas.remove(mao_pc[-1])
        contagem_de_cartas_cavadas_pc+=1
    return contagem_de_cartas_cavadas_pc


def estourou(minha_mao, pontuacao, pontuacao_pc):
    if pontuacao>21 and pontuacao_pc<=21:
        mostrar_pontuacao(minha_mao, pontuacao, mao_pc, pontuacao_pc)
        print("  Você estourou.")
        return True
    elif pontuacao_pc>21 and pontuacao<=21:
        mostrar_pontuacao(minha_mao, pontuacao, mao_pc, pontuacao_pc)
        print("  O computador estourou, você venceu.")
        return True
    elif pontuacao_pc>21 and pontuacao>21:
        mostrar_pontuacao(minha_mao, pontuacao, mao_pc, pontuacao_pc)
        print("  Ambos estouraram. Empate.")
        return True


def vitoria(minha_mao, pontuacao, pontuacao_pc):
    mostrar_pontuacao(minha_mao, pontuacao, mao_pc, pontuacao_pc)
    if pontuacao>pontuacao_pc:
        print(  "Você venceu.")
    elif pontuacao<pontuacao_pc:
        print(  "Você perdeu.")
    else:
        print(  "Empate.")
    return True


continuar_a_jogar=True
while continuar_a_jogar:
    random=SystemRandom()
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    minha_mao=[]
    mao_pc=[]
    system('cls')
    print(logo)
    minha_mao.append(cartas[random.randint(0, len(cartas)-1)])
    minha_mao.append(cartas[random.randint(0, len(cartas)-1)])
    while minha_mao[1]==minha_mao[0]:
        minha_mao[1]=random.randint(0, len(cartas)-1)
    pontuacao=minha_mao[0]+minha_mao[1]
    cartas.remove(minha_mao[0])
    cartas.remove(minha_mao[1])
    mao_pc=[cartas[random.randint(0, len(cartas)-1)]]
    pontuacao_pc=mao_pc[0]
    cartas.remove(mao_pc[0])
    mostrar_pontuacao(minha_mao, pontuacao, mao_pc, pontuacao_pc)

    while True:
        cavar=input("\nDigite 'c' para cavar mais uma carta, ou 'p' para encerrar sua jogada: ")
        if cavar=='c':
            system('cls')
            print(logo)
            pc_jogou=cavar_carta(minha_mao, mao_pc, cartas, pontuacao, pontuacao_pc)
            if pontuacao==20 and minha_mao[-1]==11:
                pontuacao+=1
            else:
                pontuacao+=minha_mao[-1]
            if pontuacao_pc==20 and mao_pc[-1]==11 and pc_jogou:
                pontuacao+=1
            elif pc_jogou:
                pontuacao_pc+=mao_pc[-1]
            if estourou(minha_mao, pontuacao, pontuacao_pc):
                break
            mostrar_pontuacao(minha_mao, pontuacao, mao_pc, pontuacao_pc)

        if cavar=='p':
            system('cls')
            print(logo)
            while True:
                if pontuacao_pc>pontuacao:
                    break
                pc_cava(cartas, mao_pc)
                if pontuacao_pc==20 and mao_pc[-1]==11:
                    pontuacao+=1
                    break
                else:
                    pontuacao_pc+=mao_pc[-1]
            if estourou(minha_mao, pontuacao, pontuacao_pc):
                break
            if vitoria(minha_mao, pontuacao, pontuacao_pc):   
                break

    choice=input("\nDeseja jogar novamente? 's' or 'n': ")
    if choice=='s':
        continuar_a_jogar=True
    else:
        continuar_a_jogar=False