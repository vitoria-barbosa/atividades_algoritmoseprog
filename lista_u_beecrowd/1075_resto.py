# Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.
def main():
    n = int(input())

    for i in range(10000):
        if i % n == 2:
            print(i)

main()