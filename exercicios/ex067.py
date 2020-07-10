# Tabuada v3.0
title = 'TABUADA'
print(f'{title:^50}')
print('=-=' * 17)
print('OBS1: Apenas números inteiros')
print('OBS2: Digite um número negativo para encerrar :)')
print('=-=' * 17)
print('')
while True:
    c = 1
    n = int(input('Digite um número: '))
    if n < 0:
        print('\nPrograma finalizado com sucesso!\n')
        break
    print('=-=' * 10)
    while True: 
        print(f'{n} x {c:2} = {n * c}')
        c += 1
        if c == 11:
            break
    print('=-=' * 10)
    print('')
