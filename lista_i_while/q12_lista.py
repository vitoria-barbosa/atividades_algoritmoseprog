# Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.
from package.io_utils import obter_numero_inteiro

def main():
    qnt = obter_numero_inteiro('Digite a quantidade de números: ')
    contador = 0
    somatorio = 0

    while contador < qnt:
        num = obter_numero_inteiro('Número: ')
        somatorio += num
        contador += 1
    
    media = somatorio / qnt
    print(f'\nSoma = {somatorio}, Média = {media}')

main()