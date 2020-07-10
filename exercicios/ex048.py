# Soma Ímpares Múltiplos de Três
from emoji import emojize
e = emojize(':fast_forward:', use_aliases=True)
s = 0
c = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        s += n
        c += 1
print('')
iz = 'Números Ímpares Múltiplos de Três'
print(f'\033[1;30m{iz:^37}')
print('\033[1;34m=-=' * 12)
print(f'\033[1;30m{e} \033[1;32mTotal de números: {c}')
print(f'\033[1;30m{e} \033[1;32mSoma total desses números: {s}')
print('\033[1;34m=-=' * 12)
