# Cálculo de Fatorial
from time import sleep
from emoji import emojize
emoji = emojize(':arrow_forward:', use_aliases=True)
emoji1 = emojize(':fast_forward:', use_aliases=True)
title = 'Cálculo Fatorial'  # Título
print('\033[1;30m=-=' * 10)
print(f'\033[1;34m{title:^30}')
print('\033[1;30m=-=' * 10)
print('')
esmain = '2'  # Primeiro Laço
fat = 1  # Contador para o Fatorial
while esmain == '2':
    es = '0'  # Segundo Laço
    n = int(input(f'\033[1;35m{emoji} Digite um número inteiro: '))
    si = 'x'
    print('')
    print(f'\033[1;33m{emoji1} Fatorial de {n}!')
    print(f'\033[1;33m{emoji1}', end=' ')
    while n >= 1:
        if n == 1:  # Condição para substituir o sinal de multiplicação por igualdade
            si = '='
        print(f'\033[1;32m{n}', end=f' {si} ')  # Comando end para continuar na mesma linha
        fat *= n
        n -= 1
    print(f'\033[1;33m{fat}')
    print('')
    while es != '1' and es != '2':
        escolha = str(input(f'''\033[1;35m{emoji} Deseja escolher outro número: 
\033[1;32m[1] Sim
\033[1;31m[2] Não
\033[1;35m{emoji} Sua escolha: ''')).strip()
        print('')
        if escolha == '2':
            print('\033[1;32mVolte sempre!')
            esmain = '1'
            es = '1'
        elif escolha == '1':
            print('\033[1;30mRedirecionando...')
            esmain = '2'
            es = '1'
            sleep(2)
        else:
            print('\033[1;31mDado inválido, tente novamente.')
            es = '3'
