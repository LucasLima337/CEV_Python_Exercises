# Função para Fatorial

def fatorial(num=1, show=False):
    '''
    * Função que calcula o fatorial de um número

    * Parâmetros:
        > num  --> número inteiro
        > show (opcional) --> valor lógico (True ou False)
            ** Caso True: Retorna a operação completa
            ** Caso False (padrão): Retorna apenas o resultado
    '''
    from math import factorial

    if num >= 0:
        if show:
            cont = num
            resp = ''
            while cont > 0:
                if cont == 1:
                    signal = f'= {factorial(num)}'
                else:
                    signal = 'x '
                resp += f'{str(cont)} {signal}'
                cont -= 1
            return resp
        else:
            return factorial(num)
    else:
        return f'Valor inserido é negativo!'


# Main Script
print(fatorial(4))
print(fatorial(5, show=True))
print(fatorial(8, False))
print(fatorial(-4))
