# Tuplas com Times de Futebol
print('')
tabela = (
    'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
    'Internacional', 'Corinthians', 'Fortaleza EC', 'Goiás', 'Bahia',
    'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro',
    'CSA', 'Chapecoense', 'Avaí'
)

print('Os 5 primeiros colocados do Campeonato Brasileiro:')
print('=-=' * 10)
for p, cinco in enumerate(tabela[:5]):
    print(f'{p + 1:>8}º - {cinco}')
print('=-=' * 10)

print('')

print('Os 4 últimos colocados do Campeonato Brasileiro:')
print('=-=' * 10)
p = 17
for quatro in tabela[-4:]:
    print(f'{p:>8}º - {quatro}')
    p += 1
print('=-=' * 10)

print('')

print('Todos os times em ordem alfabética:')
print('=-=' * 10)
for times in sorted(tabela):
    print(f'{times:^30}')
print('=-=' * 10)

print('')

print('Colocação da Chapecoense:')
pos = tabela.index('Chapecoense')
chape = tabela[pos]
print('=-=' * 10)
print(f'{pos + 1:>8}º - {chape}')
print('=-=' * 10)
