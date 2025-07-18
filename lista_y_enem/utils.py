import os

def obter_num_int(label):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero

    except ValueError:
        print("Entrada inválida. Digite um número inteiro")
        return obter_num_int(label)
    

def obter_num_em_faixa(label, min, max):
    num = obter_num_int(label)

    if min <= num <= max:
        return num
    
    else:
        print(f"Entrada inválida. Digite um número inteiro entre {min} e {max}")
        return obter_num_em_faixa(label, min, max)
    

def enter_limpar_tela():
    input("\nEnter to continue...")
    os.system('cls')


def limpar_tela():
    os.system('cls')