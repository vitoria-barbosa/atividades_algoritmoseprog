# Leia as variáveis A, Limite e R e escreva os valores menores que Limite gerados pela Progressão Geométrica que tem por valor inicial A e razão R.
from utils import obter_num_inteiro

def main():
    print('\n-------PROGRESSÃO GEOMÉTRICA-------\n')
    a = obter_num_inteiro('Número inicial: ')
    limite = obter_num_inteiro('Limite: ')
    r = obter_num_inteiro('Razão: ')
    
    termo = a

    for i in range(1000):  # número grande para garantir que cubra os termos
        if termo >= limite:
            break
        print(termo)
        termo *= r

main()