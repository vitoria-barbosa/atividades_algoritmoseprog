# Leia as variáveis A, Limite e R e escreva os valores menores que Limite gerados pela Progressão Aritmética que tem por valor inicial A e razão R.
from utils import obter_num_inteiro

def main():
    print('\n-------PROGRESSÃO ARITMÉTICA-------\n')
    a = obter_num_inteiro('Número inicial: ')
    limite = obter_num_inteiro('Limite: ')
    r = obter_num_inteiro('Razão: ')
    
    for i in range(a, limite, r):
        print(i)
        
main()