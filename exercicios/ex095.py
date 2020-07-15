# Aprimorando os Dicionários
from os import system

jogadores = list()

cont = 0
while True:
    # Lendo dados dos jogadores
    nome = str(input(f'Nome do {cont + 1}º jogador: ')).strip().title()
    qnt = int(input(f'Quantas partidas o {nome} jogou? '))

    gols = []
    for c in range(0, qnt):
        gol = int(input(f'   => Quantos gols o {nome} fez na {c + 1}ª partida? '))
        gols.append(gol)
    
    # Organizando os dados e adicionando em uma lista
    dados = {
        'nome': nome,
        'gols': gols,
        'total': sum(gols)
    }
    jogadores.append(dados)
    cont += 1

    # Perguntando se o usuário deseja cadastrar mais um jogador
    while True:
        question = str(input('\nDeseja cadastrar outro jogador? [S/N]: ')).strip().lower()[0]
        print('')
        if question in 'sn':
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N')
    
    # Exibindo uma tabela de dados dos jogadores
    if question == 'n':
        while True:
            print('=-=' * 16)
            print(f'{"ID":<5} | {"NOME":<20} | PARTIDAS JOGADAS')
            for pos, j in enumerate(jogadores):
                print('---' * 16)
                print(f'{pos:<5} | {j["nome"]:<20} | {len(j["gols"]):^15}')
            print('=-=' * 16)

            while True:
                idd = int(input('\nDigite o ID correspondente para ver mais detalhes [999 para parar]: '))
                if idd == 999:
                    break
                elif idd > len(jogadores) - 1 or idd < 0:
                    print('\nNão existe jogador com esse ID, tente novamente')
                else:
                    break

            system('clear')
            print('')

            if idd == 999:
                print('Programa encerrado!')
                break
            else:
                # Exibindo mais detalhes
                print('===' * 15)

                if jogadores[idd]['total'] == 1:
                    respgol = 'gol'
                else:
                    respgol = 'gols'
                print(f'O Jogador {jogadores[idd]["nome"]} fez um total de {jogadores[idd]["total"]} {respgol}')
                
                for j, g in enumerate(jogadores[idd]['gols']):
                    if g == 1:
                        respgol2 = 'gol'
                    else:
                        respgol2 = 'gols'
                    print(f'   => Na {j + 1}ª partida, {jogadores[idd]["nome"]} fez {g} {respgol2}')
                print('===' * 15)
        break
