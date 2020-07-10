# Dividindo valores em várias listas

lista = []
pares = []
impares = []

while True:
    num = int(input('\nDigite um número qualquer: '))
    lista.append(num)
    while True:
        question = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
        if question in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente\n')
    if question == 'n':
        for num in lista:
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)
        print('')
        print('=-=' * 15)
        lista.sort()
        print(f'Lista completa: {lista}\n')
        pares.sort()
        print(f'Lista de pares: {pares}')
        impares.sort()
        print(f'Lista de ímpares: {impares}')
        print('=-=' * 15)
        while True:
            question1 = str(input('\nDeseja reiniciar o programa? [S/N]: ')).strip().lower()[0]
            if question1 in 'sn':
                break
            else:
                print('\nDado inválido, tente novamente\n')
        if question1 == 'n':
            print('\nPrograma encerrado com sucesso!\n')
            break
        if question1 == 's':
            lista.clear()
            pares.clear()
            impares.clear()
