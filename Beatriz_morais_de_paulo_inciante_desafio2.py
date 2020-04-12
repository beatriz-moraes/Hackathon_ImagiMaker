from random import choice
nome = str(input('Qual o seu nome: '))

cont = 0
pontuacao_jogador = 0
pontuacao_pc = 0
continuar_jogando = 'S'
while continuar_jogando == 'S':
    jogada = input('Qual a sua jogada: PEDRA, PAPEL OU TESOURA: ').upper()
    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    escolhido = choice(lista)
    cont += 1

    if jogada == 'PAPEL' and escolhido == 'PEDRA':
        print('{} {} X {} Computador' .format(nome, jogada, escolhido))
        print('Você VENCEU!')
        pontuacao_jogador += 1

    elif jogada == 'PAPEL' and escolhido == 'TESOURA':
        print('{} {} X {} Computador'.format(nome, jogada, escolhido))
        print('Você PERDEU!')
        pontuacao_pc += 1

    elif jogada == 'TESOURA' and escolhido == 'PEDRA':
        print('{} {} X {} Computador'.format(nome, jogada, escolhido))
        print('Você PERDEU!')
        pontuacao_pc += 1

    elif jogada == 'TESOURA' and escolhido == 'PAPEL':
        print('{} {} X {} Computador'.format(nome, jogada, escolhido))
        print('Você VENCEU!')
        pontuacao_jogador += 1

    elif jogada == 'PEDRA' and escolhido == 'PAPEL':
        print('{} {} X {} Computador'.format(nome, jogada, escolhido))
        print('Você PERDEU!')
        pontuacao_pc += 1

    elif jogada == 'PEDRA' and escolhido == 'TESOURA':
        print('{} {} X {} Computador'.format(nome, jogada, escolhido))
        print('Você VENCEU!')
        pontuacao_jogador += 1

    elif jogada == 'PAPEL' and escolhido == 'PAPEL':
        print('{} {} X {} Computador'.format(nome, jogada, escolhido))
        print('EMPATOU!')

    elif jogada == 'TESOURA' and escolhido == 'TESOURA':
        print('{} {} X {} Computador'.format(nome, jogada, escolhido))
        print('EMPATOU!')

    elif jogada == 'PEDRA' and escolhido == 'PEDRA':
        print('{} {} X {} Computador'.format(nome, jogada, escolhido))
        print('EMPATOU!')
    else:
        print('ESCOLHA INEXISTENTE!')

    if cont == 5:
        cont = 0
        continuar_jogando = str(input('Você deseja continuar jogando [S/N]?')).upper()
        if continuar_jogando == 'N':
            print('{} {} X {} Conputador'.format(nome, pontuacao_jogador, pontuacao_pc))

