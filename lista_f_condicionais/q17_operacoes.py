# Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1 escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4 divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação escreva o quadrado dos números lidos.
from package.io_utils import obter_numero_inteiro

def main():
    n1 = obter_numero_inteiro('Digite um valor inteiro: ')
    n2 = obter_numero_inteiro('Digite outro valor inteiro: ')
    operacionar(n1, n2)


def operacionar(n1: int, n2: int):
    if n1 % n2 == 1:
        soma = n1 + n2 + (n1 % n2)
        print(f'A soma dessas variáveis mais o resto da divisão = {soma}')
    elif n1 % n2 == 2:
        if n1 % 2 == 0:
            print(f'{n1} é PAR')
        else:
            print(f'{n1} é ÍMPAR')
        if n2 % 2 == 0:
            print(f'{n2} é PAR')
        else:
            print(f'{n2} é ÍMPAR')
    elif n1 % n2 == 3:
        multiplicacao = (n1 + n2) * n1
        print(f'A multiplicação da soma dos valores lidos pelo primeiro = {multiplicacao}')
    elif n1 % n2 == 4:
        divisao = (n1 + n2) / n2
        print(f'A divisão da soma dos números pelo segundo número = {divisao}')
    else:
        quadrado_n1 = n1 ** 2
        print(f'{n1}² = {quadrado_n1}')
        quadrado_n2 = n2 ** 2
        print(f'{n2}² = {quadrado_n2}')

main()