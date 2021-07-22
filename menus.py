''' Esse aquivo contém as funções de menu com PRINT na tela '''

QUANT_PRINCIPAL = 4
QUANT_SALAS     = 6

def menuPrincipal():
    escolha = 0

    while escolha != QUANT_PRINCIPAL:
        
        darEspaco()
        print("DIGITE  UMA  OPÇÃO")
        darEspaco()

        print('[ 1 ] Gerenciamento de salas')
        print('[ 2 ] Gerenciamento de ingressos')
        print('[ 3 ] Gerenciamento de sessão')
        print('[ 4 ] Sair')


        darEspaco()
        escolha = int(input('Digite sua escolha -> '))
        darEspaco()

        if escolha == 1:
            menuSalas()

        elif  escolha == 2:
            print("EM CONSTRUÇÃO")

        elif escolha == 3:
            print("EM CONSTRUÇÃO")


def menuSalas():
    escolha = 0

    while escolha != QUANT_SALAS:
        
        darEspaco()
        print("DIGITE  UMA  OPÇÃO")
        darEspaco()

        print('[ 1 ] Cadastrar de nova sala')
        print('[ 2 ] Mostrar todas as salas')
        print('[ 3 ] Mostrar uma sala')
        print('[ 4 ] Excluir sala')
        print('[ 5 ] Alterar cadastro de uma sala')
        print('[ 6 ] Sair')


        darEspaco()
        escolha = int(input('Digite sua escolha -> '))
        darEspaco()

        if escolha == 1:
            print("EM CONSTRUÇÃO")
        elif escolha == 2:
            print("EM CONSTRUÇÃO")
        elif escolha == 3:
            print("EM CONSTRUÇÃO")
        elif escolha == 4:
            print("EM CONSTRUÇÃO")
        elif escolha == 5:
            print("EM CONSTRUÇÃO")

def darEspaco():
    print("=" *40)
