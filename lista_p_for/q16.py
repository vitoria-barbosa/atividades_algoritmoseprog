# Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.
from utils import obter_num_inteiro

def main():
    n = obter_n_maior_ou_igual_dois()
    a = 0
    b = 1

    for i in range(0, n, 1):
        print(a, end=", ") # para imprimir todos os números na mesma linha, separados por espaço.
        a, b = b, a + b
    print("fim.")


def obter_n_maior_ou_igual_dois():
    n = obter_num_inteiro('Quantidade de termos da sequência Fibonacci: ')
    if n >= 2:
        return n
    else:
        print('A quantidade deve ser maior ou igual a 2! Tente novamente: \n')
        return obter_n_maior_ou_igual_dois()

main()