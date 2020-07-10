# Aquele clássico da Média
from time import sleep
n = str(input('\033[1;30mDigite seu nome completo: ')).strip().title()
a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
m = (a + b) / 2
cor = r = ''
print('')
print(f'Olá, {n.split()[0]} {n.split()[-1]}!')
print('')
sleep(1.75)
print('CALCULANDO...\033[m')
sleep(2)
print('')
fri = 'BOLETIM ESCOLAR'
i = '=-=' * 5
print(f'\033[1;34m{i} {fri} {i}')
print(f'Nome Completo: {n}')
print(f'Primeira Nota: {a:.1f}')
print(f'Segunda Nota: {b:.1f}')
if m < 5:
    cor = '\033[1;31m'
    r = 'REPROVADO.'
elif 5 <= m <= 6.9:
    cor = '\033[1;33m'
    r = 'na RECUPERAÇÃO.'
elif m >= 7:
    cor = '\033[1;32m'
    r = 'APROVADO!'
print(f'\033[1;30mMédia Final: {cor}{m:.1f}')
print(f'Você está {r}\033[m')
print('\033[1;34m=-=' * 16)
if m >= 7:
    from pygame import mixer
    mixer.init()
    mixer.music.load('palmas.mp3')
    mixer.music.play()
    input()
