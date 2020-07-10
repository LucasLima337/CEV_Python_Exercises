# Estatísticas em produtos
title = 'Loja JBL'
print('=-=' * 10)
print(f'{title:^30}')
print('=-=' * 10)
print('')
def table():
    print('---' * 70)
    print(f'Total gasto: R${tot:.2f}\n')
    print('Produtos mais de R$1000.00:', end=' ')
    if contmil == 0:
        print('nenhum.', end='')
        resp = 'produtos'
    elif contmil == 1:
        print(f'{nomesmil[0]}.', end='')
        resp = 'produto'
    else:
        for c in range(0, len(nomesmil)):
            if c == len(nomesmil) - 2:
                pont = ' e '
            elif c == len(nomesmil) - 1:
                pont = '.'
            else:
                pont = ', '
            print(nomesmil[c], end=f'{pont}')
        resp = 'produtos'
    print(f'\nQuantos produtos mais de R$1000.00: {contmil} {resp}.\n')
    print(f'Produto mais barato: {nomebarato}')
    print(f'Preço do produto: R${barato:.2f}')
    print('---' * 70)
tot = 0
nomesmil = []
contmil = barato = 0
nomebarato = resp = ''
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preço = float(input('Preço do produto: R$'))
    tot += preço
    if preço > 1000:
        contmil += 1
        nomesmil.append(produto)
    if preço < barato or barato == 0:
        barato = preço
        nomebarato = produto
    while True:
        choice = str(input('\nDeseja continuar? [S/N]: ')).strip().lower()[0]
        if choice in 'sn':
            break
        else:
            print('\nDado inválido, tente novamente\n')
    print('')
    if choice == 'n':
        table()
        break
