# Contagem Regressiva
from emoji import emojize
import time
e = emojize(':boom:', use_aliases=True)
for i in range(10, 0, -1):
    if 5 < i:
        print(f'\033[1;31m{i}\033[m')
    elif i <= 5:
        print(f'\033[1;33m{i}\033[m')
    time.sleep(1)
print('')
print(f'\033[1;32m{e * 5} FELIZ ANO NOVOOOOO!!! {e * 5}')
print('')
a = '\033[1;35mCAIXA DE SOM'
print(f'{a:^85}')
print('\033[1;34m=-=' * 25)
from pygame import mixer
mixer.init()
mixer.music.load('fogos.mp3')
mixer.music.play()
print('\033[1;34m=-=' * 25)
input()
