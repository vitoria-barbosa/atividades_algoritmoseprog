# Leia um número e, a seguir, leia uma lista de números até achar um igual ao primeiro número lido.
from utils import obter_num_int
def main():
    n1 = obter_num_int("Digite um número: ")

    while True:
        n2 = obter_num_int("Número: ")
        if n1 == n2:
            print(f"Você escreveu um número igual ao primeiro. Fim!")
            break

main()