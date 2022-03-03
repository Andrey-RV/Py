#TODO: debugar os erros que acontecem quando o jogador escolhe continuar o jogo algumas vezes:
#      1 - o método randint falha aleatoriamente após algumas repetições;
#      2 - a mão do computador é impressa com erro após algumas repetições;

from random import SystemRandom
from os import system
from logo_e_baralho import logo, baralho_52_cartas


def setar_mao_inicial(minha_mao, mao_do_pc):
    """Adiciona duas cartas aleatórias ao jogador e uma ao computador.\n\nRetorna uma tupla com as pontuações iniciais."""
    minha_mao.append(cartas[random.randint(0, len(cartas)-1)])
    cartas.remove(minha_mao[-1])
    minha_mao.append(cartas[random.randint(0, len(cartas)-1)])
    cartas.remove(minha_mao[-1])
    mao_do_pc.append(cartas[random.randint(0, len(cartas)-1)])
    cartas.remove(mao_do_pc[-1])
    return (minha_mao[0]+minha_mao[1], mao_do_pc[0])


def mostrar_maos_e_pontuacoes(minha_mao, minha_pontuacao, mao_do_pc, pontuacao_do_pc):
    """Imprime ambas as mãos do jogador e do computador e suas respectivas pontuações."""
    print(f"  Sua mão atual é: {minha_mao}, sua pontuação atual é: {minha_pontuacao}")
    print(f"  A mão atual do computado é: {mao_do_pc}, a pontuação atual do computador é: {pontuacao_do_pc}")


def cavar_carta(minha_mao, mao_do_pc, cartas, pontuacao_do_pc):
    """Adiciona uma carta à mão do jogador e a remove do baralho.\n\nCaso a pontuação do computador seja menor que 17, uma carta também é adicionada a ele e removida do baralho.\n\nSe o computador cavou uma carta, é retornado True."""
    minha_mao.append(cartas[random.randint(0, len(cartas)-1)])
    cartas.remove(minha_mao[-1])
    if pontuacao_do_pc < 17:
        mao_do_pc.append(cartas[random.randint(0, len(cartas)-1)])
        cartas.remove(mao_do_pc[-1])
        return True
    return False


def pc_cava(mao_do_pc):
    """Adiciona uma carta para a mão do computador enquanto sua pontuação for menor do que 17."""
    mao_do_pc.append(cartas[random.randint(0, len(cartas)-1)])
    cartas.remove(mao_do_pc[-1])

def atualizar_pontuacao_do_jogador(minha_mao, minha_pontuacao):
    """Retorna a pontuação do jogador nessa rodada."""
    if minha_pontuacao == 21 and 11 in minha_mao:
        return 11
    elif minha_pontuacao != 21 and 11 in minha_mao:
        return 1
    else:
        return minha_mao[-1]


def atualizar_pontuacao_do_computador(mao_do_pc, pontuacao_do_pc):
    """Retorna a pontuação do computador nessa rodada caso ele tenha cavado uma carta."""
    if pontuacao_do_pc >= 16 and 11 in mao_do_pc:
        return 11
    elif pontuacao_do_pc < 16 and 11 in mao_do_pc:
        return 1
    else:
        return mao_do_pc[-1]


def estourou(minha_pontuacao, pontuacao_do_pc):
    """Se a pontuação do jogador ou do computador exceder 21, imprime as pontuações e discrimina quem venceu, ou se ocorreu um empate\n\nSe nenhuma das pontuações exceder 21 pontos, retorna False."""
    if minha_pontuacao > 21 and pontuacao_do_pc <= 21:
        mostrar_maos_e_pontuacoes(minha_mao, minha_pontuacao, mao_do_pc, pontuacao_do_pc)
        print("  Você estourou.")
        return True
    elif pontuacao_do_pc > 21 and minha_pontuacao <= 21:
        mostrar_maos_e_pontuacoes(minha_mao, minha_pontuacao, mao_do_pc, pontuacao_do_pc)
        print("  O computador estourou, você venceu.")
        return True
    elif pontuacao_do_pc > 21 and minha_pontuacao > 21:
        mostrar_maos_e_pontuacoes(minha_mao, minha_pontuacao, mao_do_pc, pontuacao_do_pc)
        print("  Ambos estouraram. Empate.")
        return True


def vitoria(minha_pontuacao, pontuacao_do_pc):
    """Discrimina se o jogador venceu ou perdeu com base na pontuação final entre os jogadores.\n\nRetorna True como resposta ao término do jogo."""
    mostrar_maos_e_pontuacoes(minha_mao, minha_pontuacao, mao_do_pc, pontuacao_do_pc)
    if minha_pontuacao>pontuacao_do_pc:
        print(  "Você venceu.")
    elif minha_pontuacao<pontuacao_do_pc:
        print(  "Você perdeu.")
    else:
        print(  "Empate.")
    return True


continuar_a_jogar = True
while continuar_a_jogar:
    random = SystemRandom()
    cartas = baralho_52_cartas
    minha_mao = []
    mao_do_pc = []
    pontuacao_inicial = setar_mao_inicial(minha_mao, mao_do_pc)
    minha_pontuacao = pontuacao_inicial[0]
    pontuacao_do_pc = pontuacao_inicial[1]
    system('cls')
    print(logo)
    mostrar_maos_e_pontuacoes(minha_mao, minha_pontuacao, mao_do_pc, pontuacao_do_pc)

    while True:
        cavar = input("\nDigite 'c' para cavar mais uma carta, ou 'p' para encerrar sua jogada: ")
        if cavar == 'c':
            system('cls')
            print(logo)
            pc_jogou = cavar_carta(minha_mao, mao_do_pc, cartas, pontuacao_do_pc)
            if pc_jogou:
                pontuacao_do_pc += atualizar_pontuacao_do_computador(mao_do_pc, pontuacao_do_pc)
            minha_pontuacao += atualizar_pontuacao_do_jogador(minha_mao, minha_pontuacao)
            if estourou(minha_pontuacao, pontuacao_do_pc):
                break
            mostrar_maos_e_pontuacoes(minha_mao, minha_pontuacao, mao_do_pc, pontuacao_do_pc)

        if cavar=='p':
            system('cls')
            print(logo)
            while True:
                if pontuacao_do_pc >= 17:
                    break
                pc_cava(mao_do_pc)
                pontuacao_do_pc += atualizar_pontuacao_do_computador(mao_do_pc, pontuacao_do_pc)
            if estourou(minha_pontuacao, pontuacao_do_pc) or vitoria(minha_pontuacao, pontuacao_do_pc):
                break

    choice=input("\nDeseja jogar novamente? 's' or 'n': ")
    if choice == 's':
        continuar_a_jogar=True
    else:
        continuar_a_jogar=False