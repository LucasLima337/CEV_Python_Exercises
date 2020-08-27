from utilidadesCeV.moeda import money
from utilidadesCeV.dado import dado
from os import system

system('cls')
dinheiro = dado.leiaDinheiro('Digite um valor monetário R$')
money.resumo(dinheiro, 10, 15)
