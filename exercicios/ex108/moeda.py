def aumentar(value=0, percent=0):
    '''
    --> Função que exibe um valor com um aumento percentual.
    
    --> Parâmetros:
        * value   --> Preço, salário ou um valor qualquer;
        * percent --> Percentual que deseja aumentar.
    
    --> Retorno:
        * Retorna o valor calculado com o aumento.
    '''
    resp = value + (percent / 100 * value)
    return resp

def diminuir(value=0, percent=0):
    '''
    --> Função que exibe um valor com um desconto percentual.

    --> Parâmetros:
        * value   --> Preço, salário ou um valor qualquer;
        * percent --> Percentual que deseja subtrair.
    
    --> Retorno:
        * Retorna o valor calculado com o desconto.
    '''
    resp = value - (percent / 100 * value)
    return resp

def dobro(value=0):
    '''
    --> Função que exibe o dobro de um valor.

    --> Parâmetro:
        * value --> Preço, salário ou um valor qualquer.
    
    --> Retorno:
        * Retorna o dobro do valor inserido.
    '''
    resp = value * 2
    return resp

def metade(value=0):
    '''
    --> Função que exibe a metade de um valor.

    --> Parâmetro:
        * value --> Preço, salário, ou um valor qualquer.

    --> Retorno:
        * Retorna a metade do valor inserido.
    '''
    resp = value / 2
    return resp

def moeda(value=0, coin='R$'):
    '''
    --> Função que formata um valor qualquer para um valor monetário.

    --> Parâmetros:
        * value --> Preço, salário, ou um valor qualquer;
        * coin --> Tipo da moeda.

    --> Retorno:
        * Retorna o valor formatado para o sistema monetário.
    '''
    resp = str(f'{coin}{value:.2f}').replace('.', ',')
    return resp
