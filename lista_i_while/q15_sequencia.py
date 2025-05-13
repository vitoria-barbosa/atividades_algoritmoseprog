# Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).
from package.io_utils import obter_numero_inteiro

def main():
    n = obter_numero_inteiro('Digite um número: ')
    contador = 0
    sequencia = 1
    razao = 2

    while contador < n:
        print(sequencia)
        sequencia += razao
        razao += 1
        contador += 1
    
    print('Fim.')

main()