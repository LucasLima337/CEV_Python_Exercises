# Análise de dados do grupo
title = 'Dados de um Grupo'
print('=-=' * 10)
print(f'{title:^30}')
print('=-=' * 10)
print('')
traço = '-' * 10
def table():
    print('=-=' * 25)
    print(f'Maiores de 18 anos:', end=' ')
    if people18 == 0:
        print('ninguém.', end='')
        resp = 'pessoas'
    elif people18 == 1:
        print(f'{name18[0]}.', end='')
        resp = 'pessoa'
    elif people18 > 0:
        for c in range(0, len(name18)):
            if c == len(name18) - 1:
                simbol = '. '
            else:
                simbol = ', '
            print(name18[c], end=f'{simbol}')
        resp = 'pessoas'
    print(f'\nQuantas maiores de 18: {people18} {resp}.\n')
    print(f'Homens cadastrados:', end=' ')
    if peoplehomem == 0:
        print('nenhum.', end='')
        respmen = 'homens'
    elif peoplehomem == 1:
        print(f'{namehomem[0]}.', end='')
        respmen = 'homem'
    elif peoplehomem > 0:
        for h in range(0, len(namehomem)):
            if h == len(namehomem) - 1:
                simbolh = '. '
            else:
                simbolh = ', '
            print(namehomem[h], end=f'{simbolh}')
        respmen = 'homens'
    print(f'\nQuantos homens cadastrados: {peoplehomem} {respmen}.\n')
    print('Mulheres com menos de 20 anos:', end=' ')
    if peoplemulher == 0:
        print('nenhuma.', end='')
        respwomen = 'mulheres'
    elif peoplemulher == 1:
        print(f'{namemulher[0]}.', end='')
        respwomen = 'mulher'
    elif peoplemulher > 0:
        for m in range(0, len(namemulher)):
            if m == len(namemulher) - 1:
                simbolm = '. '
            else:
                simbolm = ', '
            print(namemulher[m], end=f'{simbolm}')
        respwomen = 'mulheres'
    print(f'\nQuantas mulheres com menos de 20 anos: {peoplemulher} {respwomen}.')
    print('=-=' * 25)
cont = 1
people18 = peoplehomem = peoplemulher = 0
name18 = []
namehomem = []
namemulher = []
simbol = resp = respmen = respwomen = simbolh = simbolm = ''
while True:
    print(f'{traço} {cont}ª Pessoa {traço}')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Gênero [M/F]: ')).strip().lower()[0]
        if sexo in 'mf':
            break
        else:
            print('\nGênero inválido, tente novamente\n')
    print('-' * 31)
    print('')
    if idade > 18:
        people18 += 1
        name18.append(nome)
    if sexo == 'm':
        peoplehomem += 1
        namehomem.append(nome)
    if sexo == 'f' and idade < 20:
        peoplemulher += 1
        namemulher.append(nome)
    while True:
        question = str(input('Deseja continuar adicionando? [S/N]: ')).strip().lower()[0]
        print('')
        if question in 'sn':
            break
        else:
            print('Resposta inválida, tente novamente\n')
    if question == 'n':
        table()
        break
    cont += 1
