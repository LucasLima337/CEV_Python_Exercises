# Seno, Cosseno e Tangente
import math
from emoji import emojize
an = float(input('Digite um ângulo qualquer: '))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))
seta = emojize(':arrow_right:', use_aliases=True)
print('Ângulo digitado: {} \nSENO {} {:.2f} \nCOSSENO {} {:.2f}'.format(an, seta, s, seta, c))
print('TANGENTE {} {:.2f}'.format(seta, t))
