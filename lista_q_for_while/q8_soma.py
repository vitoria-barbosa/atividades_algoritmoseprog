# Leia um numero X e, a seguir, leia e escreva uma lista de números com o término da lista ocorrendo
# quando a soma de dois números consecutivos da lista for igual a X.
from utils import obter_num_int
def main():
    x = obter_num_int("Digite um número: ")
    anterior = 0

    while True:
        atual = obter_num_int("Número: ")
        if atual + anterior == x:
            if anterior == 0:
                continue
            print(f"A soma dos dos dois números anterioes é igual a {x}. Fim!")
            break
        anterior = atual

main()