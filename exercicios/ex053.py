# Detector de Palíndromo
import emoji
e = emoji.emojize(':arrow_forward:', use_aliases=True)
e1 = emoji.emojize(':fast_forward:', use_aliases=True)
f = str(input(f'\033[1;35m{e} Digite uma frase qualquer: ')).strip().capitalize()
fj = ''.join(f.lower().split())
i = len(fj)
fin = cor = ''
# fin = fj[::-1] --> invertendo uma palavra com fatiamento!!
for le in range(i - 1, -1, -1):
    fin += fj[le]
if fj == fin:
    cor = '\033[1;32m'
    resp = 'Palíndromo!'
else:
    cor = '\033[1;31m'
    resp = 'Não é um Palíndromo!'
print('')
print('\033[1;30m=-=' * 15)
print(f'\033[1;34m{e1} Frase digitada: {f}\n')
print(f'{e1} Frase sem espaços: {fj}')
print(f'{e1} Frase invertida: {fin}')
print('')
print(f'{cor}{e1} Resultado: {resp}')
print('\033[1;30m=-=' * 15)
