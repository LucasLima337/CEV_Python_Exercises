# Reajuste Salarial
print('=*= TRABALHO CURSO EM VÍDEO =*=')
n = input('Digite seu nome: ')
s = float(input('Digite o seu salário: R$'))
ns = s + (s * 15 / 100)
print('Olá, {}, seu salário que era de R${:.2f},'.format(n, s), end=' ')
print('agora com 15% de aumento vai ficar R${:.2f}'.format(ns))
