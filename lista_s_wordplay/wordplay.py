import os
from utils import has_no_caractere, avoids , to_lower
def main():

    menu = '''
  >>>> WORDPLAY <<<<
  1 - Palavras com Tamanho N+ (9.1)
  2 - Palavras sem Caracter Proibido (9.2)
  3 - Palavras sem Letras Proibidas (9.3)
  4 - Palavras somente com Letras Permitidas (9.4)
  5 - Palavras com Letras Obrigatórias (9.5)
  6 - Palavras com Letras em Ordem Alfabética (9.6)

  0 - Sair
 
 >>> '''

    opcao = int(input(menu))
    limpar_tela()

    while opcao != 0:
        if opcao == 1:
            palavras_com_tamanho_min()
        elif opcao == 2:
            palavras_sem_carac_proibido()
        elif opcao == 3:
            palavras_sem_letras_proibidas()
        elif opcao == 4:
            palavras_somente_com_letras_permitidas()

        print(input("\nContinue...."))
        limpar_tela()
        opcao = int(input(menu))

def palavras_somente_com_letras_permitidas():
    ...

def palavras_sem_letras_proibidas():
    total = 0
    filtro = 0
    letras_proibidas = input("Palavra proibida: ")

    file = open('palavras.txt')

    for linha in file:
        palavra = to_lower(linha.strip())
        total += 1

        if avoids(palavra, letras_proibidas):
            print(palavra)
            filtro += 1

    footer(total, filtro)


def palavras_sem_carac_proibido():
    total_palavras = 0
    palavras_filtro = 0

    caractere = input("Caractere: ")

    file = open("palavras copy.txt")

    for linha in file:

        palavra = linha.strip()
        total_palavras += 1
                
        if has_no_caractere(palavra, caractere):
            palavras_filtro += 1


def palavras_com_tamanho_min():
    total = 0
    filtro = 0
    tamanho_min = int(input("Tamanho mínimo: "))

    file = open('palavras.txt')
    for linha in file:
        palavra = linha.strip()
        total += 1

        if len(palavra) >= tamanho_min:
            print(palavra)
            filtro += 1

    footer(total, filtro)


def footer(total_palavras, palavras_filtro):
    porcentagem = palavras_filtro / total_palavras * 100
    print("-----------------------------------------------")
    print(f"Palavras filtradas/total: {palavras_filtro}/{total_palavras} ({porcentagem:.3f}%)")


def limpar_tela():
    os.system("cls")


main()