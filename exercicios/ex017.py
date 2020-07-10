# Catetos e Hipotenusa
import math
import emoji
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
tr = emoji.emojize(':triangular_ruler:', use_aliases=True)
h = math.hypot(co, ca)
print('A hipotenusa do triângulo {} é {:.2f}'.format(tr, h))
