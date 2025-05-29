from utils import obter_num_inteiro

def main():
    n = obter_num_inteiro('Digite um valor para N: ')
    numerador = 1
    somatorio = 0
    soma_negativa = 0
    soma_positiva = 0

    for denominador in range(1, n+1, 1):
        if denominador % 2 == 0:
            soma_negativa += (numerador / denominador)
        else:
            soma_positiva += (numerador / denominador)
    
    somatorio = soma_positiva - soma_negativa
    print(f'Soma das frações = {somatorio:.2f}')

main()