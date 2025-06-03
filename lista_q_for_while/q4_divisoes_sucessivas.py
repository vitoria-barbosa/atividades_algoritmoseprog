# Leia um número e divida-o por dois (sucessivamente) até que o resultado seja menor que 1. Escreva o
# resultado da última divisão efetuada.
from utils import obter_num_int
def main():
    n = obter_num_int("Digite um número: ")

    while n >= 1:
        divisao = n / 2
        n = divisao

    print(f"\nResultado da última divisão efetuada: {divisao:.2f}")

main()