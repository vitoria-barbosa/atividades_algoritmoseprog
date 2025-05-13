# Leia N e escreva todos os números inteiros de 1 a N.
from package.io_utils import obter_numero_inteiro

def main():
    n = obter_numero_inteiro('\nDigite um número inteiro: ')
    num = 1
    while num <= n:
        print(num)

        num += 1
        
main()