# Leia N e escreva todos os números inteiros pares de 1 a N.
from package.io_utils import obter_numero_inteiro

def main():
    n = obter_numero_inteiro('\nDigite um número inteiro: ')
    num = 1
    while num <= n:
        if num % 2 == 0:
         print(num)

        num += 1
    print(f'Esses são os numero pares de 1 até {n}')
    print('Fim.')
        
main()