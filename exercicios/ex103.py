# Ficha do Jogador

def ficha(nome='<desconhecido>', gols=0):
    if gols == '1':
        word = 'gol'
    else:
        word = 'gols'

    return f'O jogador {nome} marcou {gols} {word} no campeonato!'


# Main Script
nome = str(input('Digite o nome do jogador: ')).strip().title()
gols = str(input('Quantos gols ele fez no campeonato: ')).strip()

if nome == '' and gols == '':
    print(ficha())

elif nome == '':
    if gols.isalpha() or int(gols) < 0:
        print(ficha())
    else:
        print(ficha(gols=gols))

elif gols == '':
    print(ficha(nome))

else:
    if gols.isalpha() or int(gols) < 0:
        print(ficha(nome))
    else:
        print(ficha(nome, gols))
