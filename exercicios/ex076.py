# Lista de Preços com Tupla
mercadinho = (
    'Sabão', 20.75, 
    'Televisão', 2400,
    'Água Mineral', 5.30,
    'Ventilador', 450,
    'Geladeira', 1200,
    'Guarda-roupa', 3600,
    'Cama', 2100,
    'Celular', 700,
    'Computador', 9000,
    'Fone de ouvido', 50 
)

title = 'LISTA DE PRODUTOS'
print('=-=' * 15)
print(f'{title:^45}')
print('=-=' * 15)

cont = 0
for itens in mercadinho:
    if cont % 2 == 0:
        print(f'{itens:.<32}', end=' ')
    else:
        print(f'R${itens:10.2f}')
    cont += 1
print('=-=' * 15)
