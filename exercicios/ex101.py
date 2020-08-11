# Funções para votação

def line():
    print('---' * 10)

def voto(year):
    '''
    Função que verifica se uma pessoa é obrigada ou não a votar

    * Parâmetro: year -> ano de nascimento
    * Função possui retorno
    '''
    from datetime import date

    anoatual = date.today().year
    idade = anoatual - year

    if idade < 16:
        situacao = 'NEGADO'
    elif 18 > idade >= 16 or idade > 65:
        situacao = 'OPCIONAL'
    else:
        situacao = 'OBRIGATÓRIO'

    return f'Idade: {idade} | Voto: {situacao}'


# Main Script
line()
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
line()
