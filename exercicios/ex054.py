# Grupo da Maioridade
import datetime
import emoji
e = emoji.emojize(':arrow_forward:', use_aliases=True)
e1 = emoji.emojize(':fast_forward:', use_aliases=True)
at = datetime.date.today().year
i = ma = me = 0
nomesma = nomesme = ''
for p in range(1, 8):
    no = str(input(f'\033[1;35m{e} Digite o nome da {p}ª pessoa: ')).strip().title()
    an = int(input(f'{e} Digite o ano de nascimento de {no}: '))
    print('')
    i = at - an
    if i >= 18:
        nomesma += f'\033[1;32m{no} \033[1;34m|\033[m '
        ma += 1
    else:
        nomesme += f'\033[1;33m{no} \033[1;34m|\033[m '
        me += 1
print('')
fri = 'MAIORES DE IDADE'
print(f'\033[1;32m{fri:^60}')
print('\033[1;30m=-=' * 20)
print(f'\033[1;34m| {nomesma}')
print(f'\033[1;32m{e1} Quantidade de maiores de idade: {ma}')
print('\033[1;30m=-=' * 20)
print('')
wi = 'MENORES DE IDADE'
print(f'\033[1;33m{wi:^60}')
print('\033[1;30m=-=' * 20)
print(f'\033[1;34m| {nomesme}')
print(f'\033[1;33m{e1} Quantidade de menores de idade: {me}')
print('\033[1;30m=-=' * 20)
