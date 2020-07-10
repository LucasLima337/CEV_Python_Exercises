# Ano Bissexto
a = int(input('Digite um ano qualquer (0 para ver o ano atual): '))
print('')
print('=-=' * 10)
if a == 0:
    import datetime
    a = datetime.date.today().year
print(f'Ano Digitado: {a}')
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Esse ano é bissexto!')
else:
    print('Não é um ano bissexto')
print('=-=' * 10)
