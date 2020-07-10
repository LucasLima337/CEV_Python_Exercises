# Maior e menor valores
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
me = cen = ma = ''
print('')
if a < b < c:
    ma = c
    me = a
    cen = b
if a < c < b:
    ma = b
    me = a
    cen = c
if c < b < a:
    ma = a
    me = c
    cen = b
if c < a < b:
    ma = b
    me = c
    cen = a
if b < a < c:
    ma = c
    me = b
    cen = a
if b < c < a:
    ma = a
    me = b
    cen = c
print('=-=' * 10)
print(f'Números escolhidos: {me}, {cen}, {ma}')
print(f'Maior número: {ma}')
print(f'Menor número: {me}')
print('=-=' * 10)

'''a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
lista = [a, b, c]
ord = sorted(lista)
print('')
print('=-=' * 10)
print(f'Números escolhidos: {ord[0]}, {ord[1]}, {ord[2]}')
print(f'Maior número: {ord[2]}')
print(f'Menor número: {ord[0]}')
print('=-=' * 10)'''