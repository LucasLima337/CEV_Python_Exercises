# Lista composta e análise de dados
from time import sleep
import os
pessoas = list()
dados = []

while True:
    dados.append(str(input(f'Nome da {len(pessoas) + 1}ª pessoa: ')).strip().title())
    dados.append(float(input(f'Peso de {dados[0]}: ')))
    pessoas.append(dados[:])
    dados.clear()
    print('')

    while True:
        question = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
        print('')
        if question in 'sn':
            break
        else:
            print('Dado inválido, tente novamente\n')
    
    if question == 'n':
        ma = me = 0
        contmapeso = contmepeso = 0

        # Descobrindo o maior e o menor peso 
        for pos, people in enumerate(pessoas):
            if pos == 0:
                ma = people[1]
                me = people[1]
            elif people[1] > ma:
                ma = people[1]
            elif people[1] < me:
                me = people[1]

        # Contando quantas pessoas tem o maior peso;
        for people in pessoas:
            if people[1] == ma:
                contmapeso += 1
            elif people[1] == me:
                contmepeso += 1

        # Correção de plural e singular da mais pesada;
        if contmapeso > 1:
            resp2 = 'Pessoas mais pesadas'
            x2 = ' ] [ '
        elif contmapeso == 1:
            resp2 = 'Pessoa mais pesada'
            x2 = ' ]'

        # Correção de plural e singular da mais leve
        if contmepeso > 1:
            resp3 = 'Pessoas mais leves'
            x3 = ' ] [ '
        elif contmepeso == 1:
            resp3 = 'Pessoa mais leve'
            x3 = ' ]'

        # Correção do singular e plural
        if len(pessoas) == 1:
            resp1 = 'pessoa'
        else:
            resp1 = 'pessoas'
        
        print('=-=' * 30)
        print(f'Total de pessoas cadastradas: {len(pessoas)} {resp1}\n')
        
        if len(pessoas) > 1:
            print(f'{resp2}:', end=' [ ')
            contmaior = 1
            for people in pessoas:
                if contmaior == contmapeso:
                    x2 = ' ]'
                if people[1] == ma:
                    print(people[0], end=f'{x2}')
                    contmaior += 1
            print(f' ➢➢➢ {ma} kg')

            print(f'{resp3}:', end=' [ ')
            contmenor = 1
            for people in pessoas:
                if contmenor == contmepeso:
                    x3 = ' ]'
                if people[1] == me:
                    print(people[0], end=f'{x3}')
                    contmenor += 1
            print(f' ➢➢➢ {me} kg')

        else:
            print(f'Nome: {pessoas[0][0]}')
            print(f'Peso: {pessoas[0][1]} Kg')
        
        print('=-=' * 30)
        print('')

        while True:
            question2 = str(input('Deseja reiniciar o programa? [S/N]: ')).strip().lower()[0]
            if question2 in 'sn':
                break
            else:
                print('\nDado inválido, tente novamente\n')
        if question2 == 's':
            print('\nReiniciando...\n')
            sleep(2)
            os.system('clear')
            pessoas = []
            conttotal = 0
        elif question2 == 'n':
            print('\nPrograma finalizado com sucesso!\n')
            break
