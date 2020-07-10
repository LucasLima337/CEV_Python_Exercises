# Alistamento Militar
import datetime
import time
import emoji
man = emoji.emojize(':man:', use_aliases=True)
woman = emoji.emojize(':woman:', use_aliases=True)
n = str(input('\033[1;30mDigite o seu nome completo: ')).strip().title()
a = int(input('Digite o ano de seu nascimento: '))
print(f'''Qual é o seu gênero:
\033[1;34m[ 1 ] Masculino {man}
\033[1;33m[ 2 ] Feminino {woman}\033[m''')
sex = int(input('\033[1;30mDigite sua opção: '))
wi = ''
sexm = ''
anoatual = datetime.date.today().year
i = anoatual - a
print('')
print(f'Olá, {n.split()[0]} {n.split()[-1]}!')
print('')
if sex == 1 or sex == 2:
    if sex == 2:
        print('''\033[1;33mSeu alistamento não é obrigatório\033[m
\033[1;32m[ 1 ] SIM
\033[1;31m[ 2 ] NÃO''')
        sexm = int(input('\033[1;33mDeseja se alistar mesmo assim? '))
        print('')
    if sexm == 1 or sex == 1:
        time.sleep(1.75)
        print('ANALISANDO...\033[m')
        time.sleep(2)
        print('')
        print('\033[1;34m=-=' * 15)
        print(f'Nome Completo: {n}')
        print(f'Idade: {i} anos.\033[m')
        if i < 18:
            from emoji import emojize
            e = emojize(':o2:', use_aliases=True)
            print(f'\033[1;32mVocê ainda terá que se alistar. {e}')
            print(f'Seu alistamento será em {anoatual + (18 - i)}.')
            if (18 - i) > 1:
                wi = 'anos'
            elif (18 - i) == 1:
                wi = 'ano'
            print(f'Faltam {18 - i} {wi}.\033[m')
        elif i == 18:
            from emoji import emojize
            e = emojize(':o2:', use_aliases=True)
            print(f'\033[1;33mVocê está no ano de alistamento. {e}\033[m')
        else:
            from emoji import emojize
            e = emojize(':o2:', use_aliases=True)
            print(f'\033[1;31mVocê passou do tempo de alistamento! {e}')
            print(f'Seu alistamento foi em {anoatual - (i - 18)}')
            if (i - 18) > 1:
                wi = 'anos'
            elif (i - 18) == 1:
                wi = 'ano'
            print(f'Já se passaram {i - 18} {wi}.\033[m')
        print('\033[1;34m=-=' * 15)
    elif sexm == 2:
        print('\033[1;30m=-=' * 15)
        fri = 'ALISTAMENTO FINALIZADO'
        print(f'\033[1;32m{fri:^45}\033[m')
        print('\033[1;30m=-=' * 15)
    else:
        print('\033[1;31mValor inválido, tente novamente.\033[m')
else:
    print('\033[1;31mValor inválido, tente novamente.\033[m')
