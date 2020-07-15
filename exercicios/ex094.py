# Unindo dicionários e listas

pessoas = list()

somaidade = 0
cont = 1
while True:
    
    # Lendo nome, sexo e idade de uma pessoa
    nome = str(input(f'Nome da {cont}ª pessoa: ')).strip().title()

    while True:
        sexo = str(input(f'Gênero de {nome} [M/F]: ')).strip().lower()[0]
        if sexo in 'mf':
            break
        else:
            print('\nERRO! Por favor, digite apenas M ou F\n')
    
    idade = int(input(f'Idade de {nome}: '))
    somaidade += idade
    
    # Guardando os dados em um dicionário
    dados = {
        'nome': nome,
        'sexo': sexo,
        'idade': idade
    }

    # Salvando em uma lista
    pessoas.append(dados)
    cont += 1

    # Perguntando se deseja cadastrar mais alguma pessoa na lista
    while True:
        question = str(input('\nDeseja cadastrar mais alguém? [S/N]: ')).strip().lower()[0]
        print('')
        if question in 'sn':
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N')
    
    # Exibição dos dados estatísticos
    if question == 'n':
        print(f'A) Total de cadastros: {len(pessoas)} pessoas')

        media = somaidade / len(pessoas)
        print(f'B) Média de idade das pessoas: {media:.1f} anos')

        # Verificando se existem mulheres cadastradas
        mulheres = []
        for p in pessoas:
            if p['sexo'] == 'f':
                mulheres.append(p)

        if len(mulheres) == 0:
            print('C) Nenhuma mulher foi cadastrada')
        elif len(mulheres) == 1:
            print(f'C) 1 mulher cadastrada: {mulheres[0]["nome"]}')
        elif len(mulheres) > 1:
            print(f'C) {len(mulheres)} mulheres cadastradas:', end=' ')

            sinal = ''
            for pos, mulher in enumerate(mulheres):
                if pos + 1 == len(mulheres):
                    sinal = ''
                elif pos + 1 == len(mulheres) - 1:
                    sinal = ' e '
                else:
                    sinal = ', '
                print(f'{mulher["nome"]}', end=f'{sinal}')
            print('')
        
        # Verificando idades que estão acima da média
        pessoasUP = []
        for p in pessoas:
            if p['idade'] > media:
                pessoasUP.append(p)
        
        if len(pessoasUP) == 1:
            print(f'D) 1 pessoa acima da média de idade:')
            print(f'   => Nome: {pessoasUP[0]["nome"]} | Idade: {pessoasUP[0]["idade"]} | Gênero: {pessoasUP[0]["sexo"].upper()}')
        
        elif len(pessoasUP) > 1:
            print(f'D) {len(pessoasUP)} pessoas acima da média de idade:')
            for p in pessoasUP:
                print(f'   => Nome: {p["nome"]:<12} | Idade: {p["idade"]} | Gênero: {p["sexo"].upper()}')
        break
