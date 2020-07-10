# Validação de Dados
import emoji
e = emoji.emojize(':arrow_forward:', use_aliases=True)
e1 = emoji.emojize(':fast_forward:', use_aliases=True)
rox = '\033[1;35m'
s = r = ''
n = str(input(f'\033[1;35m{e} Digite o seu nome completo: ')).strip().title()
print('')
print(f'\033[1;30mOlá, {n.split()[0]} {n.split()[-1]}!\n')
#while s not in 'mf':
while s != 'm' and s != 'f':
    s = str(input(f'\033[1;35m{e} Qual é o seu sexo? (\033[1;34mM{rox}/\033[1;33mF{rox}): ')).strip().lower()[0]
    print('')
    if s != 'm' and s != 'f':
        print('\033[1;31mDado inválido, tente novamente.')
    else:
        print('\033[1;32mSexo registrado com sucesso!')
if s == 'm':
    r = '\033[1;34mMasculino'
elif s == 'f':
    r = '\033[1;33mFeminino'
print('')
print('\033[1;30m=-=' * 15)
print(f'{e1} Nome: {n}')
print(f'\033[1;30m{e1} Sexo: {r}')
print('\033[1;30m=-=' * 15)
