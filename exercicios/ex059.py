# Criando um Menu de Opções
import emoji
import time
e = emoji.emojize(':arrow_forward:', use_aliases=True)
e1 = emoji.emojize(':fast_forward:', use_aliases=True)
ep = emoji.emojize(':wave:', use_aliases=True)
ex = emoji.emojize(':x:', use_aliases=True)
fri = 'MENU DE OPÇÕES'
es = 0
es1 = 4
print('\033[1;30m=-=' * 10)
print(f'\033[1;34m{fri:^30}')
print('\033[1;30m=-=' * 10)
print('')
while es1 == 4:
    es = 0
    n1 = int(input(f'\033[1;35m{e} Digite o primeiro número: '))
    n2 = int(input(f'{e} Digite o segundo número: '))
    print('')
    while es != 5:
        print('\033[1;30m-' * 25)
        print('''\033[1;34m[1] Somar
[2] Multiplicar
[3] Quem é maior?
[4] Novos números
\033[1;31m[5] Sair do programa''')
        print('\033[1;30m-' * 25)
        es = int(input(f'\033[1;35m{e} Sua escolha: '))
        print('')
        if es == 1:
            print('\033[1;30m=-' * 15)
            print(f'\033[1;34m{e1} Primeiro número: {n1}')
            print(f'{e1} Segundo número: {n2}\n')
            print(f'\033[1;32m{e1} Resultado: {n1} + {n2} = {n1 + n2}')
            print('\033[1;30m=-' * 15)
        elif es == 2:
            print('\033[1;30m=-' * 15)
            print(f'\033[1;34m{e1} Primeiro número: {n1}')
            print(f'{e1} Segundo número: {n2}\n')
            print(f'\033[1;32m{e1} Resultado: {n1} x {n2} = {n1 * n2}')
            print('\033[1;30m=-' * 15)
        elif es == 3:
            if n1 > n2:
                resp = f'O número {n1} é maior'
            elif n2 > n1:
                resp = f'O número {n2} é maior'
            else:
                resp = f'Esses números são iguais'
            print(f'\033[1;30m=-' * 20)
            print(f'\033[1;34m{e1} Primeiro número: {n1}')
            print(f'{e1} Segundo número: {n2}\n')
            print(f'\033[1;32m{e1} Resultado: {resp}')
            print(f'\033[1;30m=-' * 20)
        elif es == 4:
            es = 5
            print('\033[1;30mRecomeçando...')
            time.sleep(2)
        elif es == 5:
            es1 = 0
            print(f'\033[1;32mVolte Sempre! {ep}')
        else:
            print(f'\033[1;31mDado inválido, tente novamente! {ex}')
        print('')
