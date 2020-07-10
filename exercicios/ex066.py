# Vários números com flag
c = s = 0
while True:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n == 999:
        break
    c += 1
    s += n
print('=-=' * 15)
print(f'Total de números digitados: {c}')
print(f'Soma total entre os números: {s}')
print('=-=' * 15)
print('\n')
