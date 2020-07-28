# Função que calcula área

# Functions #
def header():
    print('=-=' * 15)
    print(f"{'Controle de Terrenos':^45}")
    print('=-=' * 15)

def linha():
    print('=-=' * 10)

def area(w, h):
    print('')
    linha()
    print(f'Largura: {w:.2f}m')
    print(f'Altura: {h:.2f}m\n')
    print(f'Área: {w * h:.2f}m²')
    linha()
# End Functions #


# Main Script
header()
width = float(input('\nDigite a largura (m): '))
height = float(input('Digite a altura (m): '))

area(width, height)
# End Main Script #
