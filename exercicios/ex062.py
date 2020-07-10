# Super Progressão Aritmética v3.0
from time import sleep
from emoji import emojize
emoji = emojize(':arrow_forward:', use_aliases=True)
emojix = emojize(':x:', use_aliases=True)
emojibye = emojize(':wave:', use_aliases=True)
emojirepeat = emojize(':arrows_counterclockwise:', use_aliases=True)
title = 'Arithmetic Progression'
print('\033[1;30m-=-' * 10)
print(f'\033[1;34m{title:^30}')
print('\033[1;30m-=-' * 10)
print('')
loop = numterms = 0
while loop == 0:
    first = int(input(f'\033[1;35m{emoji} Type the first term: '))
    difference = int(input(f'{emoji} Type the common difference: '))
    terms = int(input(f'{emoji} Type the number of terms: '))
    cont = 1
    print('')
    if difference == 0 or terms == 0:
        print(f'\033[1;31mInvalid data, try again. {emojix}')
        print('')
        loop = 0
    else:
        while cont <= terms:
            print(f'\033[1;32m{first}', end=' ➜ ')
            first += difference
            cont += 1
            numterms += 1
        print('\033[1;33mPAUSE')
        print('')
        loopplus = 0
        while loopplus == 0:
            choice = str(input(f'''\033[1;35mWhat do you want to do right now?
\033[1;33m[1] Restart the script
\033[1;32m[2] See the others terms
\033[1;31m[3] Exit
\033[1;35m{emoji} Your choice: '''))
            print('')
            if choice == '1':
                print(f'\033[1;30m{emojirepeat} Restarting...')
                sleep(2)
                print('')
                loop = 0
                numterms = 0
                loopplus = 1
            elif choice == '2':
                loopplus1 = 1
                while loopplus1 == 1:
                    contplus = 1
                    termsplus = int(input(f'\033[1;35m{emoji} How many terms do you want to show? '))
                    if termsplus == 0:
                        print('')
                        print(f'\033[1;31mInvalid data, try again. {emojix}')
                        print('')
                        loopplus1 = 1
                    else:
                        while contplus <= termsplus:
                            print(f'\033[1;32m{first}', end=' ➜ ')
                            numterms += 1
                            first += difference
                            contplus += 1
                        print('\033[1;33mPAUSE')
                        print('')
                        loopplus = 0
                        loopplus1 = 0
            elif choice == '3':
                loopplus = 1
                loop = 1
                print(f'\33[1;30mIt was shown \033[1;32m{numterms} terms \033[1;30mby you\n')
                print(f'\033[1;32mSee you later! Bye-bye! {emojibye}')
            else:
                loopplus = 0
                print(f'\033[1;31mInvalid data, try again. {emojix}')
                print('')
