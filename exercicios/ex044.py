# Gerenciador de Pagamentos
import emoji
e = emoji.emojize(':arrow_forward:', use_aliases=True)
e1 = emoji.emojize(':fast_forward:', use_aliases=True)
e2 = emoji.emojize(':black_small_square:', use_aliases=True)
wi = '=' * 15
x = ''
while x != 0:
    fri = f'{wi} Loja do Google {wi}'
    print(f'\033[1;30m{fri}')
    n = str(input(f'\033[1;35m{e} Digite o nome do produto: ')).strip().capitalize()
    prod = float(input(f'{e} Digite o valor do produto: R$'))
    print('')
    es = int(input(f'''\033[1;30mComo deseja pagar pelo produto? (digite o número correspondente)
[1] À vista dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20% de juros)
\033[1;31m[0] Encerrar o programa
\033[1;35m{e} Sua escolha: '''))
    print('')
    if 0 <= es <= 4:
        if es == 1:
            desc = (10 / 100 * prod)
            t = prod - desc
            print('\033[1;30m-' * 40)
            print(f'\033[1;34m{e1} Produto: {n}')
            print(f'{e1} Tipo de pagamento: Dinheiro ou Cheque')
            print(f'{e1} Desconto de 10%: R${desc:.2f}')
            print('')
            print(f'\033[1;32m{e2} Total a pagar: R${t:.2f}')
            print('\033[1;30m-' * 40)
            print('')
        elif es == 2:
            desc = (5 / 100 * prod)
            t = prod - desc
            print('\033[1;30m-' * 40)
            print(f'\033[1;34m{e1} Produto: {n}')
            print(f'{e1} Tipo de pagamento: Cartão')
            print(f'{e1} Desconto de 5%: R${desc:.2f}')
            print('')
            print(f'\033[1;32m{e2} Total a pagar: R${t:.2f}')
            print('\033[1;30m-' * 40)
            print('')
        elif es == 3:
            p = prod / 2
            print('\033[1;30m-' * 40)
            print(f'\033[1;34m{e1} Produto: {n}')
            print(f'{e1} Tipo de pagamento: Cartão')
            print(f'{e1} Nenhum desconto aplicado')
            print('')
            print(f'\033[1;32m{e2} Parcelas a pagar: 2 de R${p:.2f}')
            print(f'{e2} Preço total do produto: R${prod:.2f}')
            print('\033[1;30m-' * 40)
            print('')
        elif es == 4:
            p = int(input(f'\033[1;35m{e} Em quantas vezes deseja parcelar? (3x ou mais): '))
            print('')
            ju = (20 / 100 * prod)
            t = prod + ju
            par = t / p
            print('\033[1;30m-' * 40)
            print(f'\033[1;34m{e1} Produto: {n}')
            print(f'{e1} Tipo de pagamento: Cartão')
            print(f'{e1} Juros de 20%: R${ju:.2f}')
            print('')
            print(f'\033[1;32m{e2} Parcelas a pagar: {p} de R${par:.2f}')
            print(f'{e2} Preço total do produto: R${t:.2f}')
            print('\033[1;30m-' * 40)
            print('')
        elif es == 0:
            x = 0
            print('\033[1;32mPrograma encerrado.')
            print('Volte Sempre!')
        if 0 < es <= 4:
            es1 = int(input(f'''\033[1;30mDeseja comprar outro produto?
\033[1;32m[1] Sim
\033[1;31m[2] Não
\033[1;35m{e}Sua escolha: '''))
            if es1 == 1:
                x = 1
                print('')
            else:
                x = 0
                print('')
                print('\033[1;32mPrograma encerrado.')
                print('Volte Sempre!')
    else:
        print('\033[1;31mDado inválido, tente novamente.')
        print('')
        x = 1
