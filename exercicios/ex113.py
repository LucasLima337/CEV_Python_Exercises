# Funções aprofundadas em Python

def leiaInt(msg):
    '''
    Função que lê somente números inteiros
    
    Possui um parâmetro opcional: 
        * msg --> mensagem para o usuário
    
    Retorna um número inteiro
    '''
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\n\033[1;31mERRO: Por favor, digite um número inteiro válido!\033[m\n')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário optou por não digitar um número!\033[m\n')
            return 0
        except Exception as erro:
            print(f'Erro inesperado: {erro}')
        else:
            return num

def leiaFloat(msg):
    '''
    Função que lê somente números reais
    
    Possui um parâmetro opcional: 
        * msg --> mensagem para o usuário
    
    Retorna um número flutuante
    '''
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print('\n\033[1;31mERRO: Por favor, digite um número real válido!\033[m\n')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário optou por não digitar um número!\033[m')
            return 0
        except Exception as erro:
            print(f'Erro inesperado: {erro}')
        else:
            return num

try:
    numINT = leiaInt('Digite um número inteiro: ')
    numFLOAT = leiaFloat('Digite um número flutuante: ')
except Exception as erro:
    print(f'Erro Inesperado: {erro}')
else:
    print(f'\nNúmero Inteiro: {numINT}\nNúmero Flutuante: {numFLOAT}')

