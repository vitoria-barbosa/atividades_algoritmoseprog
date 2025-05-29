from utils import obter_num_inteiro

def main():
    n = obter_num_inteiro('Digite um valor para N: ')
    numerador = 1
    denominador = n
    somatorio = 0
    soma_negativa = 0
    soma_positiva = 0
    
    for denominador in range(n, 0, -1):
        if numerador % 2 == 0:
            soma_negativa += (denominador / numerador)
        else:
            soma_positiva += (numerador / denominador)
        numerador += 1
    
    somatorio = soma_positiva - soma_negativa
    print(f'Soma das frações = {somatorio:.2f}')

main()