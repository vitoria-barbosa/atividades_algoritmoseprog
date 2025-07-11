import os


def mostar_menu():
    menu = """
 ============ Play Numbers ============ 
  
  1 - Mostrar todos os valores
  2 - Resetar vetor
  3 - Quantidade de itens no vetor
  4 - Maior e menor valor e suas posições
  5 - Somatório dos valores
  6 - Média dos valores
  7 - Valores positivos e quantidade
  8 - Valores negativos e quantidade
  9 - Atualizar o vetor seguindo uma regra
 10 - Adicionar novos valores
 11 - Remover itens por valor
 12 - Remover item por posicao
 13 - Editar valor por posição
 14 - Salvar valores em arquivo
  0 - Sair

 Sua opção >>> """
    
    return menu


def mostrar_menu2():
    menu2 = """
 > Escolha a regra que quer aplicar:

 1 - Multiplicar por um valor
 2 - Elevar a um valor (exponenciação)
 3 - Reduzir a uma fração
 4 - Substituir valores negativos por um número aleatório em uma faixa
 5 - Ordenar valores
 6 - Embaralhar valores
 
 Sua escolha >>> """
    
    return menu2


def obter_numero(label):
    entrada = input(label)

    try:
        num = int(entrada)
        return num
    
    except ValueError:
        print("Entrada inválida. Digite um número inteiro: ")
        return obter_numero(label)

def obter_num_positivo(label):
    num = obter_numero(label)

    if num >= 0:
        return num
    else:
        print("Digite um número positivo. Tente novamente: ")
        return obter_num_positivo(label)
    
def obter_num_negativo(label):
    num = obter_numero(label)

    if num >= 0:
        return num
    else:
        print("Digite um número negativo. Tente novamente: ")
        return obter_num_negativo(label)
    

def obter_num_em_faixa(label, min, max):
    num = obter_numero(label)

    if min <= num <= max:
        return num
    else:
        print(f"Digite um número entre {min} e {max}.")
        return obter_num_em_faixa(label, min, max)
    

def limpar_tela():
    input("\nEnter to continue...")
    os.system('cls')