# Calculando Descontos
p = str(input('Digite o nome do produto: '))
print('Ótima escolha!!')
prod = float(input('Digite o preço do produto: R$'))
desc = prod - (prod * (5/100))
print('O {} que antes custava R${:.2f}, agora com 5% de desconto custa R${:.2f}, aproveite!!'.format(p, prod, desc))
# fator de atualização:
# 5% de desconto = 100% - 5%    >>>   95% = 0.95      >>>   produto * 0.95 = produto com desconto
