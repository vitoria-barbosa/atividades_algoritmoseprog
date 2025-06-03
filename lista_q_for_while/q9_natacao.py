# Confira o resultado de uma competição de natação entre dois clubes. O programa deve ler o número da
# prova e a quantidade de nadadores. O fim dos dados é indicado pelo número da prova igual a 0 e
# quantidade de nadadores igual a 0. A seguir, para cada nadador deverá ler nome, classificação, tempo,
# clube (“a” ou “b”) e determinar os pontos obtidos por cada clube. Ao final, o algoritmo deve escreva os totais de pontos de cada clube, indicando o clube vencedor.
import os
from utils import obter_num_int, obter_num_int_faixa
def main():
    print("\n==== COMPETIÇÃO DE NATAÇÃO ====")
    pontos_a = 0
    pontos_b = 0
    while True:
        num_prova = obter_num_int("Número da prova: ")
        qtd_nadadores = obter_num_int("Quantidade de nadadores: ")
        if qtd_nadadores == 0 and num_prova == 0:
            break
        for i in range(1, qtd_nadadores+1, 1):
            limpar_tela()
            print(f"Nadador {i}:\n")
            nome = input("Nome do nadador: ")
            classificacao = obter_num_int_faixa("Classificação: ", 1, 4)
            tempo = float(input("Tempo de prova: "))
            clube = input("Clube(A ou B): ")
            qtd_pontos = calcular_pontos(classificacao)
            if clube.upper() == "A":
                pontos_a += qtd_pontos
            elif clube.upper() == "B":
                pontos_b += qtd_pontos
            else:
                continue
        limpar_tela()
    
    ganhador = quem_ganhou(pontos_a, pontos_b)
    resultado = f"""
 ****** RESULTADOS ******
 Clube A: {pontos_a} pontos
 Clube B: {pontos_b} pontos

 Ganhador: {ganhador}!!!!
 """
    limpar_tela()
    print(resultado)            


def calcular_pontos(lugar):
    if lugar == 1:
        return 9
    elif lugar == 2:
        return 6
    elif lugar == 3:
        return 4
    else:
        return 3
    

def quem_ganhou(pontos_a, pontos_b):
    if pontos_a > pontos_b:
        return "Clube A"
    elif pontos_b > pontos_a:
        return "Clube B"
    else:
        return "Deu empate"


def limpar_tela():
    os.system("cls")

main()