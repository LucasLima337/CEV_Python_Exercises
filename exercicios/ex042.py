# Analisando Triângulos v2.0
import time
a = float(input('\033[1;30mDigite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
print('')
print('ANALISANDO...')
time.sleep(1)
print('')
print('=-=' * 15)
print(f'Segmentos escolhidos: {a} | {b} | {c}\033[m')
if a < (b + c) and b < (a + c) and c < (a + b):
    from emoji import emojize
    e = emojize(':triangular_ruler:', use_aliases=True)
    e1 = emojize(':heavy_check_mark:', use_aliases=True)
    print(f'\033[1;32m{e} Pode formar um Triângulo! {e1}\033[m')
    if a == b == c:
        print(f'\033[1;30mTipo de Triângulo: \033[1;35mEquilátero')
    elif a == b != c or a == c != b or b == c != a:
        print(f'\033[1;30mTipo de Triângulo: \033[1;35mIsósceles')
    elif a != b != c != a:
        print(f'\033[1;30mTipo de Triângulo: \033[1;35mEscaleno')
else:
    from emoji import emojize
    e = emojize(':triangular_ruler:', use_aliases=True)
    e1 = emojize(':x:', use_aliases=True)
    print(f'\033[1;31m{e} Não pode formar um Triângulo. {e1}\033[m')
print('\033[1;30m=-=' * 15)
