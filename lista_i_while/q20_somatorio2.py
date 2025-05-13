from package.io_utils import obter_numero_inteiro

def main():
    n = obter_numero_inteiro('Digite um valor para N: ')
    numerador = 1
    denominador = 1
    somatorio = 0
    soma_negativa = 0
    soma_positiva = 0
    while denominador <= n:
        if denominador % 2 == 0:
            soma_negativa += (numerador / denominador)
        else:
            soma_positiva += (numerador / denominador)
        denominador += 1
    
    somatorio = soma_positiva - soma_negativa
    print(f'Soma das frações = {somatorio:.2f}')

main()