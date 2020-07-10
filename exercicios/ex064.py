# Tratando vários valores v1.0
title = 'Tratando Valores v1.0'
print('=-=' * 10)
print(f'{title:^30}')
print('=-=' * 10)
print('')
cont = soma = num = 0
# num = True  // Essa seria uma possibilidade
while num != 999:
    num = int(input('Digite um valor inteiro [999 para encerrar]: '))
    if num != 999:
        cont += 1
        soma += num
print('')
print('---' * 15)
print(f'Quantidade de números digitados: {cont}')
print(f'\nSoma total: {soma}')
print('---' * 15)
