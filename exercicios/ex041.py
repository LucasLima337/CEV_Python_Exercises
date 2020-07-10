# Classificando Atletas
from datetime import date
from time import sleep
n = str(input('\033[1;30mDigite o seu nome completo: ')).strip().title()
a = int(input('Digite o seu ano de nascimento: '))
anoatual = date.today().year
i = anoatual - a
print('')
sleep(1.75)
print('ANALISANDO...')
sleep(2)
print('')
print('=-=' * 15)
print(f'Nome Completo: {n}')
print(f'Idade: {i} anos.\033[m')
if i <= 9:
    print(f'\033[1;31mCategoria: MIRIM')
elif 9 < i <= 14:
    print('\033[1;32mCategoria: INFANTIL')
elif 14 < i <= 19:
    print('\033[1;33mCategoria: JUNIOR')
elif 19 < i <= 25:
    print('\033[1;34mCategoria: SÊNIOR')
else:
    print('\033[1;35mCategoria: MASTER')
print('\033[1;30m=-=' * 15)
