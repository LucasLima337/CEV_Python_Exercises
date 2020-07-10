# Contagem de Pares
a = '=-=' * 41
a1 = '\033[1;33mNúmeros Pares'
print(f'{a1:^130}')
print(f'\033[1;36m{a}')
print('\033[1;31m|', end=' ')
for n in range(2, 51, 2):
    print(f'\033[1;32m{n} \033[1;31m|\033[m', end=' ')
print(f'\n\033[1;36m{a}')
