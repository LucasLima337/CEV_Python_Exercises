# Um print especial

def escreva(msg):
    num = len(msg)

    print('~~' * num)
    print(f'{msg:^{num * 2}}')
    print('~~' * num)


escreva('Olá, Mundo!')
escreva('CeV')
escreva('We do not forgive, we do not forget')
escreva('Lucas Lima')
escreva('Oi')
