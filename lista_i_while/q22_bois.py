#Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação, nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o numero de identificação e o peso do boi mais magro e do boi mais gordo.
from package.io_utils import obter_numero_inteiro
from package.io_utils import obter_numero_float
import os

def main():
    qnt = obter_numero_inteiro('Quantas fichas: ')
    contador = 0
    maior_peso = 0
    id_maior_peso = 0
    menor_peso = float('inf')
    id_menor_peso = 0

    while contador < qnt:
        limpar_tela()
        print('======== FICHA ========')
        num_identificacao = obter_numero_inteiro('Número de identificação: ')
        nome = input('Nome do boi: ')
        peso = obter_numero_float('Peso(Kg): ')
        if peso > maior_peso:
            maior_peso = peso
            id_maior_peso = num_identificacao
        elif peso < menor_peso:
            menor_peso = peso
            id_menor_peso = num_identificacao
        contador += 1
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