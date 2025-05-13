# Leia as variáveis A, Limite e R e escreva os valores menores que Limite gerados pela Progressão Geométrica que tem por valor inicial A e razão R.
from package.io_utils import obter_numero_inteiro
from package.io_utils import obter_numero_float

def main():
    print('\n-------PROGRESSÃO GEOMÉTRICA-------\n')
    a = obter_numero_inteiro('Número inicial: ')
    limite = obter_numero_inteiro('Limite: ')
    r = obter_numero_inteiro('Razão: ')
    prog_a = a
    while prog_a <= limite:
        print(prog_a)
    
        prog_a *= r

main()