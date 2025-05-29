def main():
    input('Aperte >enter< para descobrir o somatório: ')
    numerador = 1
    somatorio = 0

    for denominador in range(1, 50+1, 1):
        somatorio += (numerador / denominador)
        numerador += 2

    print(f'Soma das frações = {somatorio:.2f}')

main()