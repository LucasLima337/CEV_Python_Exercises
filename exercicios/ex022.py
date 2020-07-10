# Analisador de Textos
n = str(input('Digite o seu nome completo: ')).strip()
t = len(n) - n.count(' ')
a = n.split()[0]
l = len(a)
# t = ''.join(n.split())      a = len(t)
# a = n[:n.find(' ')]
print(f'Olá {n.title()}, vamos analisar o seu nome!')
print('Analisando Nome...')
print('')
print('=#=' * 15)
print(f'Nome em maiúsculo: {n.upper()}')
print(f'Nome em minúsculo: {n.lower()}')
print(f'Total de letras no nome: {t} letras')
print(f'Primeiro nome: {a.capitalize()} com {l} letras')
print('=#=' * 15)
