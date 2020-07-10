# Progressão Aritmética v2.0
from time import sleep
from emoji import emojize
emoji = emojize(':fast_forward:', use_aliases=True)
emoji1 = emojize(':arrow_forward:', use_aliases=True)
title = 'Progressão Aritmética'
print('\033[1;30m=-=' * 10)
print(f'\033[1;34m{title:^30}')
print('\033[1;30m=-=' * 10)
print('')
option = '1'
while option == '1':
    erro = '0'
    first = int(input(f'\033[1;34m{emoji1} Primeiro Termo: '))
    reason = int(input(f'\033[1;34m{emoji1} Razão: '))
    last = first + 9 * reason
    print('')
    print('\033[1;34m|', end=' ')
    while first <= last:
        if first == last:
            emoji = '|'
        print(f'\033[1;32m{first}', end=f' \033[1;34m{emoji} ')
        first += reason
    print('')
    while erro == '0':
        print('')
        option = str(input(f'''\033[1;34mDeseja realizar outra progressão?
\033[1;32m[1] Sim
\033[1;31m[2] Não
\033[1;34m{emoji1} Sua escolha: '''))
        print('')
        if option == '1' or option == '2':
            if option == '1':
                print('\033[1;30mReiniciando...\n')
                sleep(2)
                print('\033[1;33m-' * 40)
                erro = '1'
            elif option == '2':
                print('\033[1;32mObrigado, volte sempre!')
                erro = '1'
        else:
            print('\033[1;31mDado inválido, tente novamente.')
            erro = '0'
