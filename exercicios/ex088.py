# Palpites para a Mega Sena
from time import sleep
from random import randint
from os import system

while True:
    megasena = []
    traco = '=-=' * 10
    msg = 'MEGA SENA'
    print(f'{traco} {msg:^5} {traco}')

    nome = str(input('Digite o seu nome: ')).strip().title()
    quant = int(input(f'\nOlá, {nome}! Quantos jogos você deseja gerar? '))

    print('\nProcessando...\n')
    sleep(1.5)

    print(f'====== As {quant} listas serão exibidas abaixo ======')
    for jogos in range(0, quant):
        lista = []
        for jogo in range(0, 6):
            num = randint(1, 60)
            while num in lista:
                num = randint(1, 60)
            if num not in lista:
                lista.append(num)
        sleep(0.9)
        print(f'Jogo {jogos + 1}: {lista}')
        megasena.append(lista[:])
        lista.clear()
    print('===' * 16)

    while True:
        question = str(input('Deseja reiniciar o programa? [S/N]: ')).strip().lower()[0]
        if question in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente\n')
    if question == 's':
        print('\nReiniciando...')
        sleep(1.5)
        system('clear')
    elif question == 'n':
        print('\nPrograma encerrado com sucesso!\n')
        break
