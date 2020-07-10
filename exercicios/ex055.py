# Maior e Menor da Sequência
from emoji import emojize
e = emojize(':arrow_forward:', use_aliases=True)
e1 = emojize(':fast_forward:', use_aliases=True)
people = ['primeira', 'segunda', 'terceira', 'quarta', 'quinta']
ma = me = 0
for p in range(0, 5):
    pe = float(input(f'\033[1;34m{e} Digite o peso da {people[p]} pessoa: '))
    if pe > ma:
        ma = pe
    if pe < me or me == 0:
        me = pe
print('')
print('\033[1;30m-' * 25)
print(f'\033[1;31m{e1} Maior Peso: {ma:.2f} kg')
print(f'\033[1;33m{e1} Menor Peso: {me:.2f} kg')
print('\033[1;30m-' * 25)
