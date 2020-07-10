# Lista ordenada sem repetições
lista = []
print('')
for c in range(1, 6):
    n = int(input(f'Digite o {c}º número: '))
    if c == 1:
        lista.append(n)
        print(f'O {n} foi adicionado ao início da lista\n')
    elif n > max(lista):
        lista.append(n)
        print(f'O {n} foi adicionado ao final da lista\n')
    elif n < min(lista):
        lista.insert(0, n)
        print(f'O {n} foi adicionado ao início da lista\n')
    else:
        for p, num in enumerate(lista):
            if n < num:
                lista.insert(p, n)
                print(f'O {n} foi adicionado na posição {p}\n')
                break

print(f'\nLista: {lista}')
