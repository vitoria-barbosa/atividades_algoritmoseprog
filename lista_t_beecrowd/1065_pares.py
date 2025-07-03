# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
def main():
    pares= 0
    for i in range(5):
        n = int(input(""))
        if n % 2 == 0:
            pares += 1

    print(f"{pares} valores pares")

main()