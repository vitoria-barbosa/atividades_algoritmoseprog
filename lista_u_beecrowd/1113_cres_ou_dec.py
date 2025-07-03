# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.
def main():
    while True:
        x, y = map(int, input().split())

        if x == y:
            break

        if x < y:
            print("Crescente")
        else:
            print("Decrescente")

main()