from utils import obter_numero_float_positivo
import os
import time

def main():
    nota = f'''\n
 ================ NOTA ===============
    '''
    valor_total = 0
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
            valor_total += valor
        elif opcao == imprimir_lista:
            limpar_tela()
            print(nota)
            print(' -------------------------------------')
            print(f'Valor total: R$ {valor_total:.2f}\n')
            analisar_parcelamento(valor_total)
            print('Opção 2 - Você pode parcelar qualquer valor em até 6x mas acrescentará juros.')
            calcular_parcelas(valor_total)
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

def analisar_parcelamento(valor_total):
    if valor_total <= 30:
        print('Opçao 0 - À vista. Esse valor não é possivel parcelar sem juros.')
    elif valor_total <= 100:
        print(f'Opção 1 - R${valor_total} é possível parcelar em até 3x sem juros.')
    else:
        print(f'Opçao 1 - R${valor_total:.2f} é possivel parcelar em até 5x sem juros.')


def calcular_parcelas(valor_total):
    opcao = int(input('Qual opção de parcelamento você escolhe: '))
    if opcao == 1:
        parcelas = int(input('Em quantas vezes irá parcelar: '))
        valor_parcelas = valor_total / parcelas
        print(f'\n{parcelas}x de R${valor_parcelas:.2f}\n')
    elif opcao == 2:
        parcelas = int(input('Em quantas vezes irá parcelar: '))
        montante = valor_total + (1 + (5/100))** parcelas
        valor_parcelas = montante / parcelas
        print(f'\n{parcelas}x de R${valor_parcelas:.2f}\n')
    elif opcao == 0:
        print(f'\n{valor_total:.2f} à vista.\n')
    else:
        print('Opção inválida. Tente novamente: ')
        return calcular_parcelas(valor_total)


# Constantes:
adicionar_item = 1
imprimir_lista = 2
sair = 0

def limpar_tela():
    os.system('cls')


def enter_to_continue():
    input('Digite <enter> para continuar....')

main()