# Função de Contador
from time import sleep

# Dentro de uma função usando o sleep, ele não mostrará nada até que ele receba uma nova linha, para forçarmos isso, basta usar o flush, que irá forçar o resultado a aparecer imediatamente.
def contador(inicio=1, fim=11, passo=1):
    print('=-=' * 15)
    print(f'{"Contagem de 1 até 10 de 1 em 1":^45}\n')

    print('|', end=' ')
    for c1 in range(inicio, fim):
        print(c1, end=' | ', flush=True)
        sleep(0.5)
    
    print('')
    print('=-=' * 15)
    print(f'{"Contagem de 10 até 0 de 2 em 2":^45}\n')

    print('|', end=' ')
    for c2 in range(10, -1, -2):
        print(c2, end=' | ', flush=True)
        sleep(0.5)
    
    print('')
    print('=-=' * 15)
    
    print('')
    print('=-=' * 15)
    print(f'{"Contagem Personalizada":^45}')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))

    if i > f:
        if -p < 0:
            pa = -p
        elif p == 0:
            pa = -1
        else:
            pa = p
    else:
        if p == 0:
            pa = 1
        else:
            pa = abs(p)

    print(f'\n{f"Contando de {i} até {f} de {abs(pa)} em {abs(pa)}":^45}\n')

    print('|', end=' ')
    for c3 in range(i, f, pa):
        print(c3, end=' | ', flush=True)
        sleep(0.5)
    if c3 + pa == f:
        print(f, end=' | ', flush=True)

    print('')


contador()
