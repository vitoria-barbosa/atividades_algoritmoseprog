# Leia um número, calcule e escreva seu fatorial.
from package.io_utils import obter_numero_inteiro

def main():
    n = obter_numero_inteiro('Digite um número inteiro: ')
    fatorial = calcular_fatorial(n)
    print(fr'{n}! = {fatorial}')

def calcular_fatorial(n):
    contador = n
    while contador > 1:
        contador -= 1
        n *= contador
    return n

main()