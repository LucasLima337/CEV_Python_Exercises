# Números Primos
from emoji import emojize
e = emojize(':arrow_forward:', use_aliases=True)
e1 = emojize(':fast_forward:', use_aliases=True)
num = int(input(f'\033[1;34m{e} Digite um número inteiro qualquer: '))
c = 0
resp = cor = ''
print('')
print('\033[1;34m|', end=' ')
for n in range(1, num + 1):
    if num % n == 0:
        cor = '\033[1;32m'
        c += 1
        if c == 2:
            resp = '\033[1;32mNúmero Primo'
        else:
            resp = '\033[1;31mNúmero NÃO Primo'
    else:
        cor = '\033[1;31m'
    print(f'{cor}{n}', end=' \033[1;34m| ')
print('')
print('')
print('\033[1;30m=-=' * 10)
print(f'{e1} Número Digitado: \033[1;34m{num}')
print(f'\033[1;30m{e1} Resposta: {resp}')
print('\033[1;30m=-=' * 10)
