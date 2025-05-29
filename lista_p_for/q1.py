# Leia N e escreva todos os números inteiros de 1 a N.
from utils import obter_num_inteiro

def main():
    n = obter_num_inteiro('\nDigite um número inteiro: ')
    
    for i in range(1, n+1, 1):
        print(i)
        
main()