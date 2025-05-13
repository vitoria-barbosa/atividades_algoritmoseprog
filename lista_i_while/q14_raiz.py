# Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o maior quadrado menor que 38 é 36 (quadrado de 6).
from package.io_utils import obter_numero_inteiro

def main():
    print('\n---- QUADRADO PERFEITO ----')
    n = obter_numero_inteiro('Digite um número: ')
    candidato = n
    maior_quadrado = qual_maior_quadrado(n)
    if maior_quadrado == candidato:
        print(f'\n{n} é um quadrado perfeito!')
    else:
        print(f'\nO maior quadrado perfeito menor que {n} é {maior_quadrado}')


def qual_maior_quadrado(candidato):
    while candidato > 0:
        for i in range(1,candidato + 1):
            if i * i == candidato:
                #print(candidato)
                return candidato# encerra a função
        candidato -= 1

main()