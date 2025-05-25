# Escreva um programa com menu para calcular
# o valor da comanda de pedidos de uma mesa em um bar.
# Operações:
# a. Inserir produtos: Cerveja (9 reais), Tira-Gosto (39 reais) e
# Água (5 reais). Entrada: “1 C” significa uma cerveja na
# conta. “3 A” 3 águas.
# b. Calcular a conta, incluindo 10% de taxa de serviço.
# c. Compras acima de 10 cervejas ou valor total superior a 200
# reais ficam isentos dos 10%
# d. Imprimir Conta: Pede quantas pessoas irão pagar.
# i. Valor da Conta e valor por pessoa.
# ii. Valor da taxa de serviço
# iii. Valor Total com taxa de serviço.
# e. Confirmar pagamento: que zera a conta da mesa.

# Começado em 21:00 de 23/05 e terminado em 12:38 do dia 24
from q1_number_utils import obter_numero_int_em_faixa
import os

def main():
    
    menu = """
 1 - Inserir Produtos
 2 - Calcular Conta
 3 - Confimar pagamento
 """
    produtos = """
 > Produtos:
 C - Cerveja............R$  9.00
 T - Tira-Gosto.........R$ 39.00
 A - Água...............R$  5.00
 """
    
    nota = """
               NOTA
 """

    inserir_produto = 1
    calcular_conta = 2

    valor_total = 0
    qtd_cervejas = 0

    while True:
        limpar_tela()
        print("\n======== BAR DA TOINHA ========")
        print(menu)
        opcao = obter_numero_int_em_faixa("Digite sua opção >> ", 1, 3)

        if opcao == inserir_produto:
            limpar_tela()
            print(produtos)
            entrada = input("> Adicione a quantidade e a inicial do seu produto: ")
            qtd_produtos = int(entrada.split()[0])
            produto = entrada.split()[1]

            if produto.upper() == "C":
                id_produto = f"\n{qtd_produtos} Cerveja\t\tR$ 9.00"
                valor = qtd_produtos * 9
                qtd_cervejas += qtd_produtos
            elif produto.upper() == "T":
                id_produto = f"\n{qtd_produtos} Tira-Gosto\t\tR$ 39.00"
                valor = qtd_produtos * 39
            elif produto.upper() == "A":
                id_produto = f"\n{qtd_produtos} Água\t\t\tR$ 5.00"
                valor = qtd_produtos * 5
            else:
                print("Produto não disponível.")
                enter_to_continue()
                continue

            
            nota += id_produto
            valor_total += valor
            
        elif opcao == calcular_conta:
            limpar_tela()
            qtd_pagantes = int(input("\n>> Quantas pessoas irão pagar: "))
            print(nota)
            taxa_servico = calcular_taxa(valor_total, qtd_cervejas)
            valor_a_pagar = valor_total + taxa_servico
            valor_pessoa = valor_a_pagar / qtd_pagantes
            conta = f"""
 ---------------------------------
 Valor conta:\t\tR$ {valor_total:.2f}
 Taxa de serviço(10%):\tR$ {taxa_servico:.2f}
 Total a pagar:\t\tR$ {valor_a_pagar:.2f}
 Valor por pessoa:\tR$ {valor_pessoa:.2f}
 """        
            print(conta)
            enter_to_continue()

        else:
            break


def calcular_taxa(valor_total, qtd_cervejas):
    if valor_total > 200 or qtd_cervejas > 10:
        return 0
    else:
        return valor_total * 0.1


def enter_to_continue():
    input("\n<ENTER> to continue....")


def limpar_tela():
    os.system("cls")

main()