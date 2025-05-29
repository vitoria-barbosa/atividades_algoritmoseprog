#Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação, nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o numero de identificação e o peso do boi mais magro e do boi mais gordo.
from utils import obter_num_inteiro
import os

def main():
    qtd = obter_num_inteiro('Quantas fichas: ')

    maior_peso = 0
    id_maior_peso = 0
    menor_peso = float('inf')
    id_menor_peso = 0

    for i in range(0, qtd, 1):
        limpar_tela()
        print('======== FICHA ========')
        num_identificacao = obter_num_inteiro('Número de identificação: ')
        nome = input('Nome do boi: ')
        peso = float(input('Peso(Kg): '))
        if peso > maior_peso:
            maior_peso = peso
            id_maior_peso = num_identificacao
        elif peso < menor_peso:
            menor_peso = peso
            id_menor_peso = num_identificacao
        limpar_tela()

    print(f"""
    ====== RESULTADO ======
    Boi com maior peso: {maior_peso}
    N° de identifição: {id_maior_peso}
    Boi com menor peso: {menor_peso}
    N° de identifição: {id_menor_peso}
    """)


def limpar_tela():
    os.system('cls')
    
main()