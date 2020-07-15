# Cadastro de Jogador de Futebol

dados = dict()

jogador = str(input('Nome do Jogador: ')).strip().title()
dados['nome'] = jogador

gols = []
qnt = int(input(f'Quantas partidas o {jogador} jogou? '))
for c in range(1, qnt + 1):
    gol = int(input(f'   Quantos gols foram feitos na {c}ª partida? '))
    gols.append(gol)

dados['gols'] = gols
dados['total'] = sum(gols)

print('=-=' * 15)
print(f'O jogador {dados["nome"]} jogou {qnt} partidas.')
for k, gol in enumerate(dados['gols']):
    print(f'   => Na {k + 1}º partida, fez {gol} gols')
print(f'Totalizando {dados["total"]} gols!')
print('=-=' * 15)
