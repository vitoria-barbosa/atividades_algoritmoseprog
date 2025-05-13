# Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.
from package.io_utils import obter_numero_inteiro

def main():
    n = obter_n_maior_ou_igual_dois()
    a = 0
    b = 1
    contador = 0

    while contador < n:
        print(a, end=" ") # para imprimir todos os números na mesma linha, separados por espaço.
        a, b = b, a + b
        contador += 1


def obter_n_maior_ou_igual_dois():
    n = obter_numero_inteiro('Quantidade de termos da sequência Fibonacci: ')
    if n >= 2:
        return n
    else:
        print('A quantidade deve ser maior ou igual a 2! Tente novamente: \n')
        return obter_n_maior_ou_igual_dois()

main()