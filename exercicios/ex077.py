# Contando vogais em Tupla
print('=-=' * 12)
print('OBS: Por favor, não usar acentos. :)')
print('=-=' * 12)
livro = ()
vogais = (
    'a', 'e', 'i', 'o', 'u', 'á', 'à', 'ã', 'â', 'é', 'è', 'ê', 'ẽ', 
    'í', 'ì', 'î', 'ĩ', 'ó', 'ò', 'ô', 'õ', 'ú', 'ù', 'û', 'ũ'
)
while True:
    quant = int(input('\nQuantas palavras você quer armazenar na tupla: '))
    for n in range(1, quant + 1):
        words = str(input(f'Digite a {n}ª palavra: ')).strip().title()
        livro += (words,)
    if n == quant:
        while True:
            choice = str(input('\nVocê deseja adicionar mais palavras? [S/N]: ')).strip().lower()[0]
            if choice in 'sn':
                break
            else:
                print('\nDado inválido, tente novamente.')
        if choice == 'n':
            # Resposta do exercício aqui :)
            print('')
            print('=-=' * 20)
            for pos in range(0, len(livro)):
                print(f'Palavra: {livro[pos]:20}', end=' ')
                print('| Vogais:', end=' ')
                for letra in livro[pos].lower():
                    if letra in vogais:
                        print(letra, end=' ')
                print('')
            print('=-=' * 20)
            break
