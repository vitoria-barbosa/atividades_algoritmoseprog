# Leia um número, calcule e escreva seu fatorial.
from utils import obter_num_inteiro

def main():
    n = obter_num_inteiro('Digite um número inteiro: ')
    fatorial = calcular_fatorial(n)
    print(fr'{n}! = {fatorial}')

def calcular_fatorial(n):
    fatorial = 1
    for i in range(n, 0, -1):
        print(i)
        fatorial *= i
    return fatorial

main()