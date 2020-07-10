# Separando dígitos de um número
num = str(input('Digite um número de 0 a 9999: '))
n = num.zfill(4)
fri = f'Número Digitado: {num}'
print('')
print(f'{fri:^30}')
print('=#=' * 10)
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')
print('=#=' * 10)
'''num = int(input('Digite um número de 0 a 9999: '))
print(f'Número digitado: {num}')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('=#=' * 10)
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
print('=#=' * 10)'''
