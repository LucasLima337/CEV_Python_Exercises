import json
dados = {}
indice = 0

def title(msg, leng=52):
    print('\033[1;37m=-=' * 15)
    print(f'\033[1;36m{msg}'.center(leng))
    print('\033[1;37m=-=' * 15)

def cadastro():
    from os import system
    from time import sleep
    title('CADASTRO DE PESSOA')
    sleep(1)

    global dados
    global indice

    try:
        nome = str(input('\033[1;37mDigite o nome: ')).strip().title()
    except KeyboardInterrupt:
        print('\n\033[1;31mO usuário optou por não digitar!\033[m\n')

    while True:
        try:
            idade = int(input('\033[1;37mDigite a idade: '))
        except (ValueError, TypeError):
            print('\n\033[1;31mPor favor, digite apenas números inteiros!\033[m\n')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário optou por não digitar!\033[m\n')
            break
        else:
            break
    
    while True:
        try:
            sexo = str(input('\033[1;37mDigite o gênero (M/F): ')).strip().upper()[0]
        except IndexError:
            print('\n\033[1;31mPor favor, digite apenas M ou F\033[m\n')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário optou por não digitar!\033[m')
            break
        else:
            if sexo in 'MF':
                break
            else:
                print('\n\033[1;31mPor favor, digite apenas M ou F\033[m\n')
    
    try:
        readjson = open('dados.json', 'r')
    except FileNotFoundError:
        dados_json = open('dados.json', 'w')
        dados[indice] = {
            'nome': nome,
            'idade': idade,
            'sexo': sexo
        }
    else:
        objeto = json.load(readjson)
        if len(objeto) != 0:
            for k in objeto.keys():
                if indice <= int(k):
                    indice += 1

        dados = objeto.copy()
        dados_json = open('dados.json', 'w')
        dados[indice] = {
            'nome': nome,
            'idade': idade,
            'sexo': sexo
        }

    json.dump(dados, dados_json, indent=4)
    system('cls')
    title('NOVA PESSOA ADICIONADA!')
    print('')


def lista():
    from time import sleep
    title('PESSOAS CADASTRADAS')
    sleep(1)

    try:
        fileJson = open('dados.json', 'r')
        dadosPessoas = json.load(fileJson)

        for pessoa in dadosPessoas.values():
            print(f'{pessoa["nome"]:<35} {pessoa["idade"]} anos')
    except FileNotFoundError:
        print('\033[1;33mNenhuma pessoa foi cadastrada!\033[m'.center(54))
    except json.decoder.JSONDecodeError:
        print('\033[1;31mPor favor, insira um bloco de chaves no arquivo "dados.json"\033[m')