# Analisador Completo
import emoji
e = emoji.emojize(':arrow_forward:', use_aliases=True)
e1 = emoji.emojize(':fast_forward:', use_aliases=True)
med = mai = contm = conth = 0
nome = resp = nomemu = resph = ''
b = '\033[1;30m'
for p in range(1, 5):
    print('\033[1;30m=-' * 25)
    n = str(input(f'\033[1;35m{e} Digite o nome da {p}ª pessoa: ')).strip().title()
    i = int(input(f'{e} Digite a idade de {n}: '))
    s = str(input(f'{e} Digite o gênero de {n} (M/F): ')).strip().lower()[0]
    print('\033[1;30m=-' * 25)
    print('')
    med += i
    if s == 'm':
        conth += 1
    if s == 'm' and i > mai:
        mai = i
        nome = n
    elif s == 'f' and i < 20:
        contm += 1
        if contm == 1:
            nomemu = f'| {n} |'
        else:
            nomemu += f' {n} |'
if conth == 0:
    resph = f'\033[1;31mNão existem \033[1;34mhomens {b}nessa lista!'
else:
    resph = f'\033[1;34m{nome} {b}é o \033[1;34mhomem mais velho {b}com \033[1;34m{mai} anos de idade'
if contm == 1:
    resp = 'mulher'
else:
    resp = 'mulheres'
print('')
print('\033[1;30m¨' * 90)
print(f'{e1} Média de Idade do grupo: \033[1;32m{(med / 4):.1f} anos')
print(f'{b}{e1} {resph}')
print(f'{b}{e1} \033[1;32m{contm} \033[1;33m{resp} {b}tem \033[1;33mmenos de 20 anos : {nomemu}')
print('\033[1;30m¨' * 90)
