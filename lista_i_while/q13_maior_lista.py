# Leia N e uma lista de N números e escreva o maior número da lista.
from package.io_utils import obter_numero_inteiro

def main():
    qnt = obter_numero_inteiro('Digite a quantidade de números: ')
    contador = 0
    maior = 0

    while contador < qnt:
        num = obter_numero_inteiro('Número: ')
        contador += 1
        if num > maior:
            maior = num
    
    print(f'\nMaior número: {maior}')

main()