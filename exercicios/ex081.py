# Extraindo dados de uma Lista

lista = []
listacopia = []
pos5 = []
cont = cont5 = 0
x = ''
while True: 
    num = int(input('\nDigite um número qualquer: '))
    lista.append(num)
    cont += 1
    while True:
        question = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
        if question in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente.\n')
    if question == 'n':
        print('')
        print('=-=' * 25)
        listacopia = lista[:]
        print(f'Lista Normal: {lista}\n')
        lista.sort()
        print(f'Lista Crescente: {lista}')
        lista.sort(reverse=True)
        print(f'Lista Decrescente: {lista}\n')
        if cont == 1:
            print('Foi digitado apenas 1 número.')
        else:
            print(f'Foram digitados {cont} números')
        for p5, num in enumerate(listacopia):
            if num == 5:
                cont5 += 1
                pos5.append(p5)
        if cont5 == 0:
            print('O número 5 não foi encontrado na lista')
        elif cont5 == 1:
            print(f'O número 5 foi encontrado na {pos5[0] + 1}ª posição')
        else:
            print(f'O número 5 foi encontrado na', end=' ')
            for pos, p in enumerate(pos5):
                if pos == len(pos5) - 1:
                    x = 'ª '
                elif pos == len(pos5) - 2:
                    x = 'ª e '
                else:
                    x = 'ª, '
                print(p + 1, end=f'{x}')
            print('posição')
        print('=-=' * 25)
        while True:
            questionfinal = str(input('\nDeseja reiniciar o programa? [S/N]: ')).strip().lower()[0]
            if questionfinal in 'sn':
                break
            else:
                print('\nDado Inválido, tente novamente.\n')
        if questionfinal == 'n':
            print('\nPrograma finalizado com sucesso!\n')
            break
        else:
            lista = []
            listacopia = []
            pos5 = []
            cont = cont5 = 0
