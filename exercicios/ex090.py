# Dicionário em Python
# condição de aprovamento >= 7
aluno = dict()
grupo = []

cont = 0
while True:
    aluno['nome'] = str(input(f'\nNome do {cont + 1}º aluno: ')).strip().title()
    aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
    if aluno['media'] >= 7:
        aluno['situacao'] = 'Aprovado'
    else:
        aluno['situacao'] = 'Reprovado'
    grupo.append(aluno.copy())

    while True:
        question = str(input('\nDeseja continuar? [S/N]: ')).strip().lower()[0]
        if question in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente!\n')

    if question == 's':
        cont += 1
    else:
        print('')
        for a in grupo:
            print('=-=' * 10)
            print(f'Nome: {a["nome"]}')
            print(f'Média: {a["media"]:.1f}')
            print(f'Situação: {a["situacao"]}')
            print('=-=' * 10)
            print('')
        break
