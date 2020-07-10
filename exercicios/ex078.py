while True:
    # Maior e Menor valores na Lista
    listanum = []
    posicaomenor = []
    posicaomaior = []
    sinal = ''

    # Lendo 5 valores e colocando-os em uma lista
    for p in range(1, 6):
        numero = int(input(f'Digite o {p}º número: '))
        listanum.append(numero)

    print('')
    print('=-=' * 10)
    # Quem é maior ou menor e exibindo a lista
    print('Lista: |', end=' ')
    for pos, num in enumerate(listanum):
        print(num, end=' | ')
        if num == min(listanum):
            posicaomenor.append(pos)
        elif num == max(listanum):
            posicaomaior.append(pos)

    print('')

    # Corrigindo Singular e Plural para o menor
    if len(posicaomenor) == 1:
        possingularME = 'Posição'
    else:
        possingularME = 'Posições'

    # Corrigindo Singular e Plural para o maior
    if len(posicaomaior) == 1:
        possingularMA = 'Posição'
    else:
        possingularMA = 'Posições'

    # Exibindo o menor valor e sua posição
    print(f'\nMenor: {min(listanum)} | {possingularME}:', end=' ')
    for pos in posicaomenor:
        if posicaomenor.index(pos) + 1 == len(posicaomenor):
            sinal = '.'
        elif posicaomenor.index(pos) + 1 == len(posicaomenor) - 1:
            sinal = ' e '
        else:
            sinal = ', '
        print(pos, end=f'{sinal}')

    # Exibindo o maior valor e sua posição
    print(f'\nMaior: {max(listanum)} | {possingularMA}:', end=' ')
    for pos in posicaomaior:
        if posicaomaior.index(pos) + 1 == len(posicaomaior):
            sinal = '.'
        elif posicaomaior.index(pos) + 1 == len(posicaomaior) - 1:
            sinal = ' e '
        else:
            sinal = ', '
        print(pos, end=f'{sinal}')

    print('')
    print('=-=' * 10)

    # Pergunta para encerrar o programa
    while True:
        pergunta = str(input('\nDeseja reiniciar o programa? [S/N]: ')).strip().lower()[0]
        if pergunta in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente!')
    if pergunta == 'n':
        print('\nPrograma encerrado com sucesso!\n')
        break
