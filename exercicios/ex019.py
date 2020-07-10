# Sorteando um item na lista
import random
import emoji
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
x = random.choice(lista)
e = emoji.emojize(':white_check_mark:', use_aliases=True)
print('O aluno escolhido foi {} {}'.format(x, e))
