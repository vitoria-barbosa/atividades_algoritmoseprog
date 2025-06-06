# Contexto/Problema: Um pequeno restaurante precisa gerenciar seu estoque de alimentos, registrando
# a data de compra e a data de validade de cada item. O programa deve permitir que o usuário insira
# vários itens no estoque. Para cada item, o usuário deve informar o nome do alimento, a quantidade, a
# data de compra e a data de validade (ambas no formato DD/MM/AAAA). O programa deve identificar e
# listar para cada alimento quantos dias ainda de validade próxima ou já está vencido. (Considerar 12
# meses de 30 dias exatos cada ano)
# ● Entrada: O usuário deve informar a quantidade de itens a serem cadastrados no estoque. Para cada
# item, o usuário deve informar o nome, a quantidade, a data de compra e a data de validade.
# ● Saída Esperada: Uma lista de alimentos que estão com a validade próxima ou vencidos, informando o
# nome do alimento e a data de validade.
from utils import obter_num_int
def main():
    print("\n ====== CONTROLE DE ESTOQUE ======")
    qtd_itens = obter_num_int("Quantidade de itens que serão cadastrados: ")
    lista_vencidos = " "

    for i in range(1, qtd_itens+1, 1):
        print(f"\nItem {i}: ")
        nome = input("Nome do alimento: ")
        quantidade = obter_num_int("Quantidade: ")
        entrada_compra = input("Data de compra(DD/MM/AAAA): ")
        entrada_validade = input("Data de validade(DD/MM/AAAA): ")
        dia_compra = int(entrada_compra.split("/")[0]) 
        mes_compra = int(entrada_compra.split("/")[1])
        ano_compra = int(entrada_compra.split("/")[2])
        dia_val = int(entrada_validade.split("/")[0]) 
        mes_val = int(entrada_validade.split("/")[1])
        ano_val = int(entrada_validade.split("/")[2])

        if analisar_validade(dia_compra, mes_compra, ano_compra, dia_val, mes_val, ano_val):
            lista_vencidos += f"\n{nome}\t\tValidade: {entrada_validade}"

    print(f"""
 --------------------------------------------------
 ALIMENTOS QUE VENCERAM OU ESTÃO PRÓXIMOS DE VENCER:
 {lista_vencidos}
 """)


def analisar_validade(dia_compra, mes_compra, ano_compra, dia_val, mes_val, ano_val) -> bool:

    qtd_dias = 30 - dia_compra + dia_val

    if ano_val < ano_compra:
        return True
    elif ano_val == ano_compra:
        if mes_val < mes_compra:
            return True
        elif qtd_dias <= 20: # considerado próximo da validade com 20 dias ou menos.
            return True
        else:
            return False
    else:
        return False


main()