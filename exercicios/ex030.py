# Par ou Ímpar?
n = int(input('Digite um número inteiro: '))
print('')
print('=-=' * 10)
print('Número Digitado: {}'.format(n))
if n % 2 == 0:
    print('Número Par')
    print('=-=' * 10)
else:
    print('Número Ímpar')
    print('=-=' * 10)
