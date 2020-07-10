# Número por Extenso
numeros = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
    'treze', 'quatorze', 'quinze', 'desesseis', 'desessete',
    'dezoito', 'dezenove', 'vinte'
)

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('\nPor favor, insira um número dentro do limite\n')
    print(f'\nNúmero escolhido: {numeros[num]}\n')
    while True:
        choice = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
        if choice not in 'sn':
            print('\nDado inválido, tente novamente\n')
        else:
            break
    if choice == 'n':
        print('\nPrograma encerrado com sucesso!\n')
        break
    else:
        print('')
