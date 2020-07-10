# Soma dos pares
from emoji import emojize
e = emojize(':arrow_forward:', use_aliases=True)
e1 = emojize(':fast_forward:', use_aliases=True)
lista = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto']
s = 0
c = 0
for n in range(0, 6):
    num = int(input(f'\033[1;34m{e} Digite o {lista[n]} número: '))
    if num % 2 == 0:
        s += num
        c += 1
if c == 1:
    stri = f'\033[1;32m{e1:>2} Você digitou um único número par: {s}'
elif c == 0:
    stri = f'\033[1;31m{e1:>3} Você não digitou nenhum número par'
else:
    stri = f'\033[1;32m{e1:>5} Soma dos {c} números pares: {s}'
print('')
print('\033[1;30m-' * 40)
print(f'{stri}')
print('\033[1;30m-' * 40)
