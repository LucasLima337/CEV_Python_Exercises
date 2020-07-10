# Simulador de Caixa Eletrônico
title = 'Caixa Eletrônico'
cedtitle = 'Cédulas disponíveis'
cinvin = 'R$50.00 | R$20.00'
deum = 'R$10.00 | R$1.00'
print('=-=' * 10)
print(f'{title:^30}\n')
print(f'{cedtitle:^30}\n\n{cinvin:^30}\n{deum:^29}')
print('=-=' * 10)
print('')
def notas():
    dinheiro = money
    print('')
    print('-' * 35)
    print(f'Dinheiro desejado: R${dinheiro:.2f}\n')
    ced = 50
    contced = 0
    while True:
        if dinheiro >= ced:
            dinheiro -= ced
            contced += 1
        else:
            if contced > 0:
                print(f'{contced} cédulas de R${ced:.2f}')
            contced = 0
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            else:
                break
    print('-' * 35)
while True:
    money = int(input('Quantos reais deseja sacar? R$'))
    notas()
    while True:
        choice = str(input('\nDeseja sacar mais algum valor? [S/N]: ')).strip().lower()[0]
        print('')
        if choice in 'sn':
            break
        else:
            print('Dado inválido, tente novamente.\n')
    if choice == 'n':
        print('Programa encerrado com sucesso!\n')
        break
