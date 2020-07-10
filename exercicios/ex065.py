# Maior e Menor valores
choice = 's'
cont = soma = maior = menor = 0
while choice != 'n':
    num = int(input('\nDigite um número inteiro: '))
    cont += 1
    soma += num
    loop = 1
    if num > maior:
        maior = num
    elif num < menor or menor == 0:
        menor = num
    while loop == 1:
        choice = str(input('Deseja continuar? [Sim/Não] ')).strip().lower()[0]
        if choice != 's' and choice != 'n':
            print('\nDado inválido, tente novamente.')
            print('')
            loop = 1
        else:
            loop = 0
média = (soma / cont)
print('')
print('=-=' * 10)
print(f'Média dos valores: {média:.1f}\n')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}\n')
print(f'Total de números digitados: {cont}')
print('=-=' * 10)
