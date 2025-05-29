# Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).
from utils import obter_num_inteiro

def main():
    n = obter_num_inteiro('Digite um número: ')
    sequencia = 1
    razao = 2

    for i in range(0, n, 1):
        print(f"{sequencia}," , end=' ')
        sequencia += razao
        razao += 1
    
    print('Fim.')

main()