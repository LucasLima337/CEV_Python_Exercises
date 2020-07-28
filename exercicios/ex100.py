# Funções para sortear e somar
from random import randint
from time import sleep


def linha():
    print('=-=' * 15)

def sorteia():
    c = 0
    while c < 5:
        num = randint(0, 20)
        numeros.append(num)
        c += 1

def somaPar(lista):
    par = soma = 0

    linha()
    print(f'{"Sorteando 5 números...":^47}\n')

    # Exibição dos números
    print('|', end=' ')
    for num in lista:
        if num % 2 == 0:
            print(f'\033[1;32m{num}\033[m', end=' | ', flush=True)
            par += 1
            soma += num
        else:
            print(num, end=' | ', flush=True)
        sleep(0.75)
    print('\n')
    # Fim da exibição dos números
    
    # Ajuste de mensagem
    if par == 0:
        print('Não foi encontrado nenhum número par...')
    elif par == 1:
        print('Foi encontrado 1 número par...')
    else:
        print(f'Foram encontrados {par} números pares...')
    # Fim do ajuste de mensagem
    
    print(f'Soma dos Pares: {soma}')
    linha()


# Main Script
numeros = list()

sorteia()
somaPar(numeros)
