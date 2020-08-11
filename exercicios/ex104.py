# Validando entrada de dados em Python

def leiaInt(input2):
    while True:
        num = input(input2)

        if num.isnumeric() or '-' in num and '.' not in num:
            return f'\033[1;32m{num}\033[m'
        else:
            print('\033[1;31mERRO! Por favor, somente números inteiros!\033[m\n')


# Main Script
n = leiaInt('Digite um número: ')
print(f'\nVocê digitou o número {n}')
