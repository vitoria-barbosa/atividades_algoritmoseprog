from package.io_utils import obter_numero_inteiro

def main():
    n = obter_numero_inteiro('Digite um número: ')

    contador = n
    soma = n

    while contador >= 1:
        contador -= 1
        soma += contador
    
    print(f'\nA soma de {n} + todos os inteiros até  1 é igual a {soma}')


main()