# Primeiro e último nome de uma pessoa
nome = str(input('Digite seu nome completo: ')).strip().title()
p = nome.split()[0]
u = nome.split()[-1]
l = len(nome) - nome.count(' ')
print('')
print('=#=' * 15)
print(f'Nome Completo: {nome}')
print(f'Primeiro Nome: {p}')
print(f'Último Nome: {u}')
print(f'Total de letras do nome: {l} letras')
print('=#=' * 15)
