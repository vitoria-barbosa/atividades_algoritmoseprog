# Leia 2 números inteiros e escreva a multiplicação dos mesmos, sem que o operador de multiplicação (*)
# seja utilizado.
from utils import obter_num_int
def main():
    n = obter_num_int("Digite um número: ")
    m = obter_num_int(f"Digite um número para multiplicar {n}: ")
    multiplicacao = 0

    for i in range(0, m):
        multiplicacao += n

    print("Resultado:", multiplicacao)

main()