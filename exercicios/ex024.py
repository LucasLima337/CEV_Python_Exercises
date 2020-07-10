city = str(input('Digite o nome de uma cidade: ')).strip().lower()
s = city.split()[0]
a = 'santo' in s
print('')
print('=#=' * 13)
print(f'Cidade Escolhida: {city.title()}')
print(f'Começa com a palavra "SANTO"?: {a}')
print('=#=' * 13)
