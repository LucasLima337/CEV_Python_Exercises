from lib.cadastro import cadastro, lista, title

def menu():
    '''
    Função menu
    Objetivo: Exibir um menu de cadastro aos usuários

    Funcionalidades:
        * Cadastrar uma nova pessoa;
        * Listar as pessoas cadastradas
        * Encerrar o programa
    '''
    from os import system

    while True:
        title('MENU DE CADASTROS')
        
        print('''\033[1;32m[ 1 ] Cadastrar uma pessoa
\033[1;33m[ 2 ] Listas as pessoas
\033[1;31m[ 3 ] Encerrar o programa''')

        print('\033[1;37m=-=\033[m' * 15)

        while True:
            try:
                choice = int(input('\n\033[1;37mSua escolha: '))
            except (ValueError, TypeError):
                print('\n\033[1;31mPor favor, digite apenas um dos números válidos!\033[m')
            except KeyboardInterrupt:
                print('\n\033[1;31mO usuário optou por não digitar!\033[m')
                break
            else:
                if choice == 1:
                    system('cls')
                    cadastro()
                    break
                elif choice == 2:
                    system('cls')
                    lista()
                    break
                elif choice == 3:
                    system('cls')
                    title('Programa encerrado com sucesso!')
                    break
                else:
                    print('\n\033[1;31mPor favor, digite apenas um dos números válidos!\033[m')
        if choice == 3:
            break