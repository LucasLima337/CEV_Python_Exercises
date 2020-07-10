# Aumentos múltiplos
n = str(input('Digite o nome completo do funcionário: ')).strip().title()
s = float(input('Digite o salário do funcionário: R$'))
print('')
print(f'Olá, {n.split()[0]} {n.split()[-1]}!')
print('')
if s > 1250:
    p = 10
    a = s + (10 / 100 * s)
    print('=-=' * 15)
    print(f'Nome Completo: {n}')
    print(f'Salário: R${s:.2f}')
    print(f'Salário com {p}% de aumento: R${a:.2f}')
else:
    if s == 0:
        print('=-=' * 15)
        print('Valor inválido, tente novamente!')
    else:
        p = 15
        a = s + (15 / 100 * s)
        print('=-=' * 15)
        print(f'Nome Completo: {n}')
        print(f'Salário: R${s:.2f}')
        print(f'Salário com {p}% de aumento: R${a:.2f}')
print('=-=' * 15)
