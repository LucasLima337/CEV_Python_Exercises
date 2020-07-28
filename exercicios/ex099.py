# Função que descobre o maior
from time import sleep


def line():
    print('=-=' * 15)

def pluralSingular(length, word):
    if length == 1:
        if word[-1] == 's':
            return word.replace(word[-1], '')
        else:
            return word
    else:
        if word[-1] == 's':
            return word
        else:
            word += 's'
            return word

def maior(*numeros):
    comprimento = len(numeros)

    # Ajuste de palavras no plural e singular #
    if len(numeros) == 1:
        resp = 'Foi'
    else:
        resp = 'Foram'

    word1 = pluralSingular(comprimento, "digitados")
    word2 = pluralSingular(comprimento, "número")
    # Fim do ajuste de palavras no plural e singular #

    # Exibição dos parâmetros passados e o maior deles #
    if comprimento != 0:
        line()
        print(f'{f"{resp} {word1} {comprimento} {word2}":^45}\n')
        print('|', end=' ')
        for num in numeros:
            print(f'{num}', end=' | ', flush=True)
            sleep(0.75)
        print('')
        print(f'\nMaior número: {max(numeros)}')
        line()
    else:
        print('Nenhum número foi digitado!')
    # Fim da exibição dos parâmetros passados e o maior deles #

    print('')


# Main Script
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
