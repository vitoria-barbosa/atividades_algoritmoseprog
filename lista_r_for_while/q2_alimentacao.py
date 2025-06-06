# Entrada: O usuário deve informar a quantidade de pessoas para análise. Para cada pessoa, o usuário
# deve informar a quantidade de alimentos que serão adicionados ao cardápio e, para cada alimento, seu
# nome (correspondente aos dados iniciais) e a quantidade em gramas. Valide o nome do alimento, se
# inválido pedir novamente.
# ● Saída Esperada: Para cada pessoa, o total de calorias e proteínas consumidas. Ao final, indicar qual
# pessoa teve o maior e o menor consumo calórico total.
import os
from utils import obter_num_int
def main():
    show_cardapio()
    qtd_pessoas = obter_num_int("Quantidade de pessoas: ")
    alimentos = {
 "arroz": {"calorias": 130, "proteinas": 2.7}, "frango": {"calorias": 165, "proteinas": 31},
 "ovo": {"calorias": 155, "proteinas": 13}, "feijao": {"calorias": 132, "proteinas": 9},
 "carne": {"calorias": 200, "proteinas": 28}, "pao": {"calorias": 265, "proteinas": 8},
 "queijo": {"calorias": 300, "proteinas": 22}, "banana": {"calorias": 89, "proteinas": 1.1},
 "batata cozida": {"calorias": 86, "proteinas": 2}, "leite": {"calorias": 61, "proteinas": 3.2}
 }
    total_calorias = 0
    total_proteinas = 0
    maior_caloria = 0
    menor_caloria = 100000

    for pessoa in range(1, qtd_pessoas+1, 1):
        print(f"\nPessoa {pessoa}: ")
        qtd_alimentos = obter_num_int("Quantos alimentos quer adicionar: ")

        for i in range(1, qtd_alimentos+1, 1):
            print(f"\nAlimento {i}:")
            nome = obter_alimento_valido(alimentos)
            gramas = obter_num_int("Quantidade em grama que ingeriu: ")
            valor_calorico = alimentos[nome]["calorias"] # para 100 gramas
            valor_proteico = alimentos[nome]["proteinas"]
            calorias = (valor_calorico / 100) * gramas
            proteinas = (valor_proteico / 100) * gramas
            total_calorias += calorias
            total_proteinas += proteinas

        if total_calorias > maior_caloria:
            maior_caloria = pessoa
        if total_calorias < menor_caloria:
            menor_caloria = pessoa

        print(f"""
 Total Calorias: {total_calorias} 
 Total Proteínas: {total_proteinas}
 """)

    print(f"""
 > Maior consumo calórico total: Pessoa {maior_caloria}
 > Menor consumo calórico total: Pessoa {menor_caloria}
 """)


def obter_alimento_valido(alimentos):
    nome = input("Nome do alimento: ")

    for chave in alimentos:
        if nome == chave:
            return nome

    print("Alimento não consta no cardápio. Digite outro alimento: ")
    return obter_alimento_valido(alimentos)


def show_cardapio():
    cardapio = """
 ======== CARDÁPIO ========
 > Arroz\t> Pão
 > Frango\t> Queijo
 > Banana\t> Ovo
 > Feijão\t> Batata cozida
 > Carne\t> Leite
 """
    print(cardapio)

main()