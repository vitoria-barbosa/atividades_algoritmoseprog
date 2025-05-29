from utils import obter_num_inteiro

def main():
    n = obter_num_inteiro('Digite um número: ')
    soma = 0
    
    for i in range(n, 0, -1):
        soma += i

    print(f'\nA soma de {n} + todos os inteiros até  1 é igual a {soma}')

main()