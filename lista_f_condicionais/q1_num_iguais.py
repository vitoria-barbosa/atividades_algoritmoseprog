# Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números

def main():
    n1 = obter_numero_inteiro('Digite um número:')
    n2 = obter_numero_inteiro('Digite outro número:')
    n3 = obter_numero_inteiro('Digite mais um número:')

    contar_numeros_iguais(n1, n2, n3)
    

def obter_numero_inteiro(label: str):
  return int(input(label))


def sao_iguais(n1,n2):
    return n1 == n2

def contar_numeros_iguais(n1,n2,n3):
    if sao_iguais(n1,n2) and sao_iguais(n1,n3) and sao_iguais(n2,n3) == True:
        print('\nOs três números são iguais!')

    elif sao_iguais(n1,n2) == True or sao_iguais(n1,n3) == True or sao_iguais(n2,n3) == True:
        print('\nHá dois números iguais.')

    else:
        print('\nOs três números são diferentes.')

main()