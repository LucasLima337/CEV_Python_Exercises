# Antecessor e Sucessor
print('--' * 20)
print('=' * 3, 'PARA NÚMEROS INTEIROS', '=' * 3)
num = int(input('Digite o primeiro número: '))
a = num - 1
s = num + 1
print('Primeiro número escolhido: {}'.format(num))
print('Antecessor: {} \nSucessor: {}'.format(a, s))
print('--' * 20)
print('=' * 3, 'PARA NÚMEROS REAIS', '=' * 3)
num2 = float(input('Digite o segundo número: '))
a2 = num2 - 0.1
s2 = num2 + 0.1
print('Segundo número escolhido: {}'.format(num2))
print('Antecessor: {:.1f} \nSucessor: {}'.format(a2, s2))
print('--' * 20)
