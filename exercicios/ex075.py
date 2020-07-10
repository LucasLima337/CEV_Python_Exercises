# Análise de dados em uma Tupla
numeração = ('primeiro', 'segundo', 'terceiro', 'quarto')
tupla = ()
tuplapar = ()

contpar = 0
# Utilizei (n,) para armazenar valores dentro de uma tupla
for num in range(0, len(numeração)):
    n = int(input(f'Digite o {numeração[num]} valor: '))
    tupla += (n,)
    if n % 2 == 0:
        tuplapar += (n,)
        contpar += 1

print('')

# Mostrando uma Tupla
for numtupla in tupla:
    print(numtupla, end=' ')

# Verificando quantas vezes apareceu o número 9
if tupla.count(9) == 1:
    v = 'vez'
else:
    v = 'vezes'
print(f'\n\nO número 9 apareceu {tupla.count(9)} {v}')

# Verificando em que posição apareceu o primeiro 3
if tupla.count(3) == 0:
    resp = 'O número 3 não foi encontrado'
else:
    resp = f'O primeiro número 3 foi encontrado na {tupla.index(3) + 1}ª posição'
print(resp)

# Exibindo os números pares da tupla
if contpar == 0:
    resppar = 'Não foi armazenado nenhum número par na tupla'
elif contpar == 1:
    resppar = f'Número par armazenado: {tuplapar[0]}'
else:
    resppar = 'Números pares armazenados:'

print(resppar, end=' ')
if contpar > 1:
    for par in tuplapar:
        print(par, end=' ')
print('')
