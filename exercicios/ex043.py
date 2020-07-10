# Índice de Massa Corporal
import time
n = str(input('\033[1;30mDigite seu nome completo: ')).strip().title()
p = float(input('Digite seu peso (Kg): '))
h = float(input('Digite sua altura (m): '))
imc = p / h ** 2
print('')
print(f'Olá, {n.split()[0]} {n.split()[-1]}!')
print('')
time.sleep(1.3)
print('CALCULANDO IMC...\033[m')
time.sleep(2)
print('')
print('\033[1;34m=-=' * 15)
print(f'Nome Completo: {n}')
print(f'Peso: {p} Kg')
print(f'Altura: {h}m\033[m')
if imc < 18.5:
    print(f'\033[1;31mSeu IMC é {imc:.1f}')
    print('Você está Abaixo do Peso.')
elif 18.5 <= imc < 25:
    print(f'\033[1;32mSeu IMC é {imc:.1f}')
    print('Você está no Peso Ideal.')
elif 25 <= imc < 30:
    print(f'\033[1;33mSeu IMC é {imc:.1f}')
    print('Você está com Sobrepeso.')
elif 30 <= imc < 40:
    print(f'\033[1;33mSeu IMC é {imc:.1f}')
    print('Você está com Obesidade.')
else:
    print(f'\033[1;31mSeu IMC é {imc:.1f}')
    print('Você está com Obesidade Mórbida.')
print('\033[1;34m=-=' * 15)
