# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.
def main():
    x = int(input())
    y = int(input())

    soma = 0
    candidato = x - 1
    while candidato > y:
        if not candidato % 2 == 0:
            soma += candidato

        candidato -= 1

    print(soma)

main()