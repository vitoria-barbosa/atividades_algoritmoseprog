from package.io_utils import obter_numero_inteiro

def main():
    input('Aperte >enter< para descobrir o somatório: ')
    numerador = 1
    denominador = 1
    somatorio = 0

    while denominador <= 50:
        somatorio += (numerador / denominador)
        numerador += 2
        denominador += 1
    
    print(f'Soma das frações = {somatorio:.2f}')

main()