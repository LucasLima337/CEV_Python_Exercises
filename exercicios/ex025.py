# Procurando uma string dentro de outra
n = str(input('Digite o seu nome completo: ')).strip().lower()
r = 'silva' in n.split()
print('')
print('=#=' * 17)
print(f'Nome Completo: {n.title()}')
print(f'Seu nome tem "SILVA"? {r}')
print('=#=' * 17)
