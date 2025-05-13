from utils import obter_numero_float_positivo
import os
import time

def main():
    nota = f'''\n
 ================ NOTA ===============
    '''
    
    while True:
        time.sleep(0.6)
        limpar_tela()
        show_menu()
        opcao = int(input('Digite sua opção >>> '))
        if opcao == sair:
            break
        elif opcao == adicionar_item:
            limpar_tela()
            print('------------------------')
            item = input('Item: ')
            especificacao = input('Especificação: ')
            valor = obter_numero_float_positivo('Valor(R$): ')
            print('------------------------')
            produto = f'''\n{item}\t({especificacao})\t\tR$ {valor}'''
            nota += produto
        elif opcao == imprimir_lista:
            print(nota)
            print(' -------------------------------------\n')
            enter_to_continue()
            limpar_tela()
        

def show_menu():
    menu = f"""
 ======= CAIXA ======
 1 - Adicionar produto
 2 - Imprimir Nota
 0 - Sair
    """
    print(menu)


def limpar_tela():
    os.system('cls')


def enter_to_continue():
    input('Digite <enter> para continuar....')

# Constantes:
adicionar_item = 1
imprimir_lista = 2
sair = 0

main()