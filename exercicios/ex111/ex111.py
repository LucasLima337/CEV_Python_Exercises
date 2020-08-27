# Transformando módulos em pacotes

from utilidadesCeV.moeda import money

p = float(input('Digite um preço R$'))
money.resumo(p, 20, 12)
