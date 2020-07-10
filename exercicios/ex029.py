# Radar eletrônico
import time
n = str(input('Digite o seu nome: ')).strip().title()
v = int(input('Digite a velocidade do seu carro na via: '))
print('')
time.sleep(1.5)
print('PROCESSANDO...')
time.sleep(2)
print('=-=' * 15)
print(f'Nome do Condutor: {n}')
print(f'Velocidade em que estava na via: {v}km/h')
if 40 <= v <= 80:
    print('Radar eletrônico: Não Multado')
    print('Tenha um bom dia! Dirija com segurança!')
    print('=-=' * 15)
else:
    if v > 80:
        m = (v - 80) * 7
        print('Radar eletrônico: Multado')
        print('Velocidade superior a máxima')
        print(f'Total a pagar: R${m:.2f}')
        print('=-=' * 15)
    if v < 40:
        m = (40 - v) * 7
        print('Radar eletrônico: Multado')
        print('Velocidade inferior a mínima')
        print(f'Total a pagar: R${m:.2f}')
        print('=-=' * 15)
