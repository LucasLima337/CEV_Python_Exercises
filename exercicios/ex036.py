# Aprovando Empréstimo
import time
n = str(input('\033[1;30mDigite seu nome completo: ')).strip().title()
vc = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o seu salário: R$'))
a = int(input('Digite por quantos anos irá pagar: '))
prest = vc / (a * 12)
print('')
print(f'Olá, {n.split()[0]} {n.split()[-1]}!\033[m')
print('')
time.sleep(0.75)
print('\033[1;30mANALISANDO...\033[m')
time.sleep(2)
print('')
print('\033[1;30m=-=\033[m' * 15)
if prest > ((30 / 100) * s):
    from emoji import emojize
    e = emojize(':x:', use_aliases=True)
    print(f'\033[1;31mEMPRÉSTIMO NEGADO! {e}')
    print('Prestação excedeu 30% do salário!')
    print(f'PRESTAÇÃO: R${prest:.2f}/mês\033[m')
elif prest < ((30 / 100) * s):
    from emoji import emojize
    e = emojize(':heavy_check_mark:', use_aliases=True)
    print(f'\033[1;32mEMPRÉSTIMO APROVADO! {e}\033[m')
    print(f'\033[1;34mNome Completo: {n}')
    print(f'Salário: R${s:.2f}')
    print(f'Valor da Casa: R${vc:.2f}')
    print(f'Anos de Pagamento: {a} anos.\033[m')
    print(f'\033[1;32mPRESTAÇÃO: R${prest:.2f}/mês\033[m')
print('\033[1;30m=-=\033[m' * 15)
