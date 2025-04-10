# Leia 2 frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

import math

def principal():
    print('>Fração 1:')
    n1 = int(input('Numerador: '))
    d1 = int(input('Denominador: '))
    print('\n>Fração 2:')
    n2 = int(input('Numerador: '))
    d2 = int(input('Denominador: '))
    
    mmc = math.lcm(d1,d2)
    soma_numerador = ((mmc / d1) * n1) + ((mmc / d2) * n2)

    print('\n>>>>>>>>SOMA DE FRAÇÕES<<<<<<<<')
    print(f'\n{n1}/{d1} + {n2}/{d2} = {soma_numerador:.0f}/{mmc}')

principal()
