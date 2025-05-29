# Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o maior quadrado menor que 38 é 36 (quadrado de 6).
from utils import obter_num_inteiro

def main():
    print('\n---- QUADRADO PERFEITO ----')
    n = obter_num_inteiro('Digite um número: ')

    maior_quadrado = qual_maior_quadrado(n)
    if maior_quadrado == n:
        print(f'\n{n} é um quadrado perfeito!')
    else:
        print(f'\nO maior quadrado perfeito menor que {n} é {maior_quadrado}')


def qual_maior_quadrado(n):
    for n in range(n, 0, -1):
        for i in range(1,n + 1, 1):
            if i * i == n:
                return n

main()