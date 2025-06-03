# Leia dois números X e N. A seguir, escreva o resultado das divisões de X por N onde, após cada
# divisão, X passa a ter como conteúdo o resultado da divisão anterior e N é decrementado de 1 em 1, até
# chegar a 2.
from utils import obter_num_int
def main():
    x = obter_num_int("X: ")
    n = obter_num_int("N: ")

    while n > 2:
        divisao = x / n
        print(divisao, end=" ")
        x = divisao
        n -= 1

main()