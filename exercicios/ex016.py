# Quebrando um número
from math import trunc
from emoji import emojize
dd = emojize(':point_right:', use_aliases=True)
de = emojize(':point_left:', use_aliases=True)
n = float(input('Digite um número real: '))
print('O número digitado foi {} {} e sua porção inteira é {} {}'.format(dd, n, trunc(n), de))

# podemos printar a parte inteira com o comando int(n)
