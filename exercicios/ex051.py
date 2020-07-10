# Progressão Aritmética
from emoji import emojize
e = emojize(':arrow_forward:', use_aliases=True)
stri = f'10 PRIMEIROS TERMOS DA PA'
print('\033[1;34m=-=' * 10)
print(f'{stri:^30}')
print('=-=' * 10)
print('')
p = int(input(f'\033[1;35m{e} Primeiro termo: '))
r = int(input(f'{e} Razão: '))
u = p + 9 * r
print('')
print('\033[1;31m-' * 56)
print('| ', end='')
for pa in range(p, u + r, r):
    print(f'\033[1;32m{pa}', end=' → ')
print('FIM \033[1;33m|')
print('-' * 56)
