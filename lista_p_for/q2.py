# Leia N e escreva todos os números inteiros pares de 1 a N.
from utils import obter_num_inteiro

def main():
    n = obter_num_inteiro('\nDigite um número inteiro: ')
    
    print(f'\nEsses são os numero pares de 1 até {n}')
    for i in range(2, n+1, 2):
        print(i)
        
    print('Fim.')
        
main()