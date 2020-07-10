# Analisando Triângulo v1.0
import time
a = float(input('\033[1;30mComprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta:\033[m '))
print('')
print('\033[33m=-=\033[33m' * 10)
print(f'\033[30mPrimeira reta: {a}m')
print(f'Segunda reta: {b}m')
print(f'Terceira reta: {c}m\033[m')
print('\033[1;33m=-=\033[33m' * 10)
print('')
print('\033[1;30mANALISANDO...\033[m')
time.sleep(2.5)
print('')
print('\033[1;33m=-=\033[m' * 13)
if a < (b + c) and b < (a + c) and c < (a + b):
    from emoji import emojize
    e = emojize(':triangular_ruler:', use_aliases=True)
    e1 = emojize(':heavy_check_mark:', use_aliases=True)
    print(f'\033[1;32m{e} Pode formar um triângulo!! {e1}\033[m')
    print('\033[1;33m=-=\033[m' * 13)
else:
    import emoji
    e = emoji.emojize(':triangular_ruler:', use_aliases=True)
    e1 = emoji.emojize(':heavy_multiplication_x:', use_aliases=True)
    print(f'\033[1;31m{e} Não pode formar um triângulo. {e1}\033[m')
    print('\033[1;33m=-=\033[m' * 13)
