# Jogo da Adivinhação v1.0
import random
n = str(input('Digite o seu nome: ')).strip().title()
pc = random.randint(0, 5)
print('')
print('=#=' * 20)
print(f'Olá {n}, eu sou seu computador e vou te propor um desafio.')
print('Você consegue adivinhar em qual número pensei entre 0 e 5?')
print('=#=' * 20)
print('')
print('Então vamos lá!!')
print('')
num = int(input('Escolha um número: '))
print('')
if num <= 5:
    import time
    print('PROCESSANDO...')
    time.sleep(2)
    print('=#=' * 10)
    print(f'Número Escolhido: {num} \nComputador Escolheu: {pc}')
    if num == pc:
        from emoji import emojize
        e = emojize(':thumbsup:', use_aliases=True)
        print(f'Parabéns, você acertou!! {e}')
        print('=#=' * 10)
        from pygame import mixer
        mixer.init()
        mixer.music.load('palmas.mp3')
        mixer.music.play()
        input()
    else:
        from emoji import emojize
        e = emojize(':thumbsdown:', use_aliases=True)
        print(f'Opa, você errou! {e}')
        print('=#=' * 10)
        from pygame import mixer
        mixer.init()
        mixer.music.load('errou.mp3')
        mixer.music.play()
        input()
else:
    print('Número inválido, tente novamente.')
