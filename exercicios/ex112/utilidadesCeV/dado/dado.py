def leiaDinheiro(msg):
    while True:
        money = str(input(msg)).strip()
        num = money

        if '.' in money:
            num = money.replace('.', '')
        elif ',' in money:
            num = money.replace(',', '')
            money = money.replace(',', '.')
        
        if num.isnumeric():
            return float(money)
        else:
            print(f'\nERRO: "{money}" não é um valor válido!\n')
