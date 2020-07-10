# Boletim com listas compostas

turma = []
aluno = []

cont = 0
while True:
    aluno.append(str(input(f'Nome do {cont + 1}º aluno: ')).strip().title())
    print(f'\nNotas de {aluno[0]}:')
    aluno.append(float(input('1ª nota: ')))
    aluno.append(float(input('2ª nota: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    turma.append(aluno[:])
    cont += 1
    aluno.clear()
    print('')
    
    while True:
        question = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
        if question in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente!\n')
    if question == 'n':
        print(f'\n| {"Nº":^7} | {"Nome":^35} | {"Média":^10} |')
        print('-' * 62)
        for pos, pessoa in enumerate(turma):
            print(f'| {pos:^7} | {pessoa[0]:^35} | {pessoa[3]:^10.1f} |')
            print('-' * 62)

        while True:
            question1 = int(input('\nDigite o número correspondente para visualizar as notas [999 para encerrar]: '))

            print('')
            if question1 < len(turma):
                for pos, pessoa in enumerate(turma):
                    if question1 == pos:
                        print('=-=' * 10)
                        print(f'Nome: {pessoa[0]}')
                        print(f'Nota1: {pessoa[1]}')
                        print(f'Nota2: {pessoa[2]}')
                        print('=-=' * 10)
                        break
            elif question1 == 999:
                print('Programa encerrado com sucesso!\n')
                break
            else:
                print('Número inválido, tente novamente!')
        break
