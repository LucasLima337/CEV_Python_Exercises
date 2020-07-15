# Jogo de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter # Para ordernar o dicionário

players = dict()

msg = f'{"=-=" * 5} Sorteio {"=-=" * 5}'
print(f'{msg}')

# Sorteando os números para os 4 jogadores
for c in range(1, 5):
    sleep(1)
    dado = randint(1, 6)
    print(f'Jogador {c}: resultado: {dado}')
    players[f'jogador_{c}'] = dado

print(f'\n{"=-=" * 3} Colocações dos jogadores {"=-=" * 3}')


# Exibindo os jogadores por ordem de maior número no dado
# itemgetter ordena a tupla com base na primeira posição (value)
pos = 1
for k, v in sorted(players.items(), key=itemgetter(1), reverse=True):
    print(f'{pos}º Colocado: {k} | Número: {v}')
    sleep(1)
    pos += 1
