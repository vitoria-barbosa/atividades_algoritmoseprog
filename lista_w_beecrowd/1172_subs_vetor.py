# A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.
# Saída
# Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.
def main():
    array = []
    for i in range(10):
        x = int(input())
        if x <= 0:
            x = 1
        array.append(x)

        print(f"X[{i}] = {x}")


main()