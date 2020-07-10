# Jogo do Par ou Ímpar
from random import randint
title = 'Jogo Par ou Ímpar'
print('=-=' * 10)
print(f'{title:^30}\n')
print('OBS: Apenas números inteiros')
print('OBS: Apenas números de 0 a 10')
print('=-=' * 10)
print('')
def vitoria():
    print(f'{numvitoria}')
    print('---' * 12)
def tabela():
    print('---' * 12)
    print(f'Jogador: {player}')
    print(f'Jogada: {resp}\n')
    print(f'Computador: {pc}')
    print(f'Jogada: {respc}\n')
    print(f'Soma dos valores: {soma} | {pi}')
    print(f'Resultado: {resultado}')
    print('---' * 12)
vit = soma = 0
numvitoria = pi = ''
while True:
    pc = randint(0, 10)
    while True:
        player = int(input('Digite um número: '))
        if 0 <= player <= 10:
            break
        else:
            print('\nPor favor, digite um número entre 0 e 10!\n')
    while True:
        jogada = str(input('Você quer Par ou Ímpar [P/I]: ')).strip().lower()[0]
        if jogada in 'pi':
            break
        else:
            print('\nPor favor, digite P para PAR ou I para Ímpar!\n')
    soma = player + pc
    if jogada == 'p':
        resp = 'PAR'
        respc = 'ÍMPAR'
        if soma % 2 == 0:
            vit += 1
            pi = 'PAR'
            resultado = 'Você ganhou!'
            tabela()
            print('')
        else:
            pi = 'ÍMPAR'
            resultado = 'Você perdeu!'
            tabela()
            if vit == 0:
                numvitoria = 'Você não venceu nenhuma vez :('
            elif vit == 1:
                numvitoria = 'Você venceu 1 vez!'
            else:
                numvitoria = f'Você venceu {vit} vezes!'
            vitoria()
            break
    elif jogada == 'i':
        resp = 'ÍMPAR'
        respc = 'PAR'
        if soma % 2 == 1:
            vit += 1
            pi = 'ÍMPAR'
            resultado = 'Você ganhou!'
            tabela()
            print('')
        else:
            pi = 'PAR'
            resultado = 'Você perdeu!'
            tabela()
            if vit == 0:
                numvitoria = 'Você não venceu nenhuma vez :('
            elif vit == 1:
                numvitoria = 'Você venceu 1 vez!'
            else:
                numvitoria = f'Você venceu {vit} vezes!'
            vitoria()
            break
