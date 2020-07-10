# Tabuada v2.0
from emoji import emojize
e = emojize(':arrow_forward:', use_aliases=True)
n = int(input(f'\033[1;35m{e} Digite um número para ver sua tabuada: '))
print('\033[1;30m=-=' * 10)
for t in range(1, 11):
    print(f'\033[1;33m{n:>10} x {t:2} = {n * t}')
print('\033[1;30m=-=' * 10)
