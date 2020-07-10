# Validando expressões matemáticas

exp = str(input('Digite uma expressão qualquer: ')).strip()
lp = exp.count('(')
rp = exp.count(')')

pare = []
if lp == rp:
    for p in exp:
        if p == '(' or p == ')':
            pare.append(p)
    if pare[0] == '(' and pare[-1] == ')':
        print('Essa expressão é válida!')
    else:
        print('Essa expressão é inválida!')
else:
    print('Essa expressão é inválida!')
