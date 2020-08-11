# Sistema interativo de ajuda em Python
from time import sleep

def header():
    print('\033[1;30;42m=-=' * 10)
    print(f"{'SISTEMAS DE AJUDA PYHELP':^30}")
    print('=-=' * 10)

def printf(word):
    msg = f'Acessando o manual do comando "{word}"'
    print('\033[1;37;44m==' * (len(word) + 20))
    print(f'{msg:^{(len(word) + 20) * 2}}')
    print('==' * (len(word) + 20))
    print('\033[m')


# Main Script
while True:
    header()
    word = str(input('\033[mFunção ou Biblioteca >> ')).strip().lower()
    if word == 'fim':
        print('\033[1;37;45m=-=' * 15)
        print(f"{'Programa encerrado com sucesso!':^45}")
        print('=-=' * 15)
        print('\033[m')
        break
    else:
        printf(word)
        sleep(1.5)
        help(word)
