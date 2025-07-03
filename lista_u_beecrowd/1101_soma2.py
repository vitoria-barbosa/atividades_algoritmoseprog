# Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).
def main():
    while True:
        m, n = map(int, input().split())
        if m <= 0 or n <= 0:
            break
        menor = m if m < n else n
        maior = n if n > m else m
        soma = 0

        for i in range(menor, maior+1):
            soma += i
            print(f"{i}", end=" ")

        print(f"Sum={soma}")

main()