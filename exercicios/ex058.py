# Jogo da Advinhação v2.0
from random import randint
from emoji import emojize
from time import sleep
es = 0
erro = 1
player = 11
e = emojize(':arrow_forward:', use_aliases=True)
e1 = emojize(':fast_forward:', use_aliases=True)
et = emojize(':wave:', use_aliases=True)
fri = 'JOGO DA ADVINHAÇÃO v2.0'
print('\033[1;31m-' * 30)
print(f'\033[1;33m{fri:^30}')
print('\033[1;34m-' * 30)
n = str(input(f'\n\033[1;35m{e} Insira o seu nome completo para jogar: ')).strip().title()
print(f'\n\033[1;31mComputador: - Olá, \033[1;32m{n.split()[0]} {n.split()[-1]}\033[1;31m!!', end=' ')
print('Vejo que veio aqui para tentar me vencer!')
print('\033[1;30mDigitando...')
sleep(1)
print('\033[1;31mComputador: - Pois saiba que esse será um grande desafio para você!')
print('\033[1;30mDigitando...')
sleep(1.5)
print('\033[1;31mComputador: - Será que você é bom o suficiente para \033[1;32madvinhar', end=' ')
print('\033[1;31mem que número eu pensei \033[1;32mentre 0 e 10\033[1;31m?')
pc = randint(0, 10)
while es != 1 and es != 2:
    es = int(input(f'''
\033[1;32m[1] Me sinto pronto!
\033[1;31m[2] Agora não...
\033[1;35m{e} Sua escolha: '''))
    print('')
    if es == 1 or es == 2:
        if es == 1:
            print('\033[1;31mComputador: - Então vamos lá!')
            print('\033[1;31mComputador: - Diga em qual \033[1;32mnúmero \033[1;31mpensei!')
            while player != pc:
                print('')
                player = int(input(f'\033[1;32m{e} Seu palpite: '))
                print('')
                if player > 10:
                    print('\033[1;30mDigitando...')
                    sleep(0.9)
                    print('\033[1;31mComputador: - Você está digitando um número acima do limite que eu coloquei!')
                    print('\033[1;31mComputador: - Tente outra vez!')
                elif player != pc:
                    erro += 1
                    print('\033[1;31mComputador: Opa! Você errou hehehe...')
                    if player < pc:
                        print('\033[1;30mDigitando...')
                        sleep(0.9)
                        print('\033[1;31mComputador: - O número que pensei é \033[1;32mmaior \033[1;31mque isso!')
                        print('\033[1;31mComputador: - Tente outra vez!')
                    elif player > pc:
                        print('\033[1;30mDigitando...')
                        sleep(0.9)
                        print('\033[1;31mComputador: - O número que pensei é \033[1;32mmenor \033[1;31mque isso!')
                        print('\033[1;31mComputador: - Tente outra vez!')
                elif player == pc:
                    print(f'\033[1;31mComputador: - \033[1;32mParabéns, {n.split()[0]}!')
                    print('\033[1;30mDigitando...')
                    sleep(2)
                    print('\033[1;31mComputador: - \033[1;32mVocê \033[1;31mconseguiu me vencer.')
                    print('\033[1;30mDigitando...')
                    sleep(2)
                    print('\033[1;31mComputador: - Analise aqui suas estatísticas:')
                    print('\033[1;32mCarregando...')
                    sleep(2)
                    print('')
                    print('\033[1;30m=-=' * 20)
                    print(f'\033[1;32m{e1} Player: {n} \n{e1} Pensou no número: {player}\n')
                    print(f'\033[1;31m{e1} Adversário: Computador \n{e1} Pensou no número: {pc}\n')
                    print(f'\033[1;32m{e1} Palpites para vencer: {erro} tentativas')
                    print('\033[1;30m=-=' * 20)
        elif es == 2:
            print(f'\033[1;32mAté a próxima, {n.split()[0]}! {et}')
    else:
        print('\033[1;31mDado inválido, tente novamente.')
        es = 0
