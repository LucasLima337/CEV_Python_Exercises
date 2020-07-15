# Cadastro de Trabalhador em Python
from datetime import date
from os import system

pessoas = dict()

idd = 1 
while True:
    nome = str(input('Digite o seu nome completo: ')).strip().title()
    ano = int(input(f'Digite o ano do seu nascimento, {nome.split()[0]}: '))

    # Calculando a idade
    anoatual = date.today().year
    idade = anoatual - ano

    # adicionando os dados no dicionário
    pessoas[idd] = {
        'nome': nome,
        'idade': f'{idade} anos'
    }

    ctps = int(input('Digite o número da sua carteira de trabalho (0 caso não tenha): '))

    # Salvando os dados da carteira de trabalho
    if ctps != 0:
        contrato = int(input('Digite o ano de contratação: '))
        salario = float(input('Digite o seu salário: R$'))
        pessoas[idd]['ctps'] = {
            'número': ctps,
            'contrato': contrato,
            'salario': f'R${salario:.2f}',
            'aposentadoria': f'{ idade + (contrato + 35) - anoatual} anos'
        }
    else:
        pessoas[idd]['ctps'] = 'Não possui carteira'

    while True:
        question = str(input('\nDeseja cadastrar mais alguém? [S/N]: ')).strip().lower()[0]
        print('')
        if question in 'sn':
            break
        else:
            print('Resposta inválida, tente novamente!')
    
    if question == 's':
        idd += 1
    else:
        # exibindo os cadastros
        system('clear') # Diferente para cada sistema operacional | windows > cls
        while True:
            print('=-=' * 20)
            for k, v in pessoas.items():
                print(f'id: {k} | nome: {v["nome"]}')
            print('=-=' * 20)

            id2 = int(input('\nDigite o id correspondente para ver mais detalhes [0 para sair]: '))
            system('clear')

            if id2 == 0:
                break
            
            else:
                print('=-=' * 20)
                for k, v in pessoas[id2].items():
                    if k == 'ctps' and type(pessoas[id2]['ctps']) == dict:
                        print('\nCtps:')
                        for k, v in pessoas[id2]['ctps'].items():
                            print(f'{k}: {v}')
                    else:
                        print(f'{k}: {v}')
                print('=-=' * 20)

        print('\nPrograma encerrado com sucesso!\n')
        break
